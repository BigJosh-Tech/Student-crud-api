import unittest
from app import app, db, Student


class TestStudentAPI(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_healthcheck(self):
        response = self.app.get("/api/v1/healthcheck")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

    def test_create_student(self):
        response = self.app.post(
            "/api/v1/students", json={"name": "Alice", "age": 20, "grade": "A"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["name"], "Alice")
        self.assertEqual(response.json["age"], 20)
        self.assertEqual(response.json["grade"], "A")

    def test_get_students(self):
        with app.app_context():
            db.session.add(Student(name="Bob", age=21, grade="B"))
            db.session.commit()

        response = self.app.get("/api/v1/students")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]["name"], "Bob")

    def test_get_student_by_id(self):
        with app.app_context():
            student = Student(name="Charlie", age=22, grade="C")
            db.session.add(student)
            db.session.commit()
            db.session.refresh(student)  # Must be inside the context

        response = self.app.get(f"/api/v1/students/{student.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Charlie")
        self.assertEqual(response.json["age"], 22)
        self.assertEqual(response.json["grade"], "C")

    def test_update_student(self):
        with app.app_context():
            student = Student(name="Diana", age=23, grade="D")
            db.session.add(student)
            db.session.commit()
            db.session.refresh(student)  # Must be inside the context

        response = self.app.put(
            f"/api/v1/students/{student.id}",
            json={"name": "Diana Updated", "grade": "A"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Diana Updated")
        self.assertEqual(response.json["grade"], "A")
        self.assertEqual(response.json["age"], 23)  # Unchanged

    def test_delete_student(self):
        with app.app_context():
            student = Student(name="Eve", age=24, grade="E")
            db.session.add(student)
            db.session.commit()
            db.session.refresh(student)  # Must be inside the context

        response = self.app.delete(f"/api/v1/students/{student.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Student deleted successfully"})

        # Verify student is no longer in the database
        response = self.app.get(f"/api/v1/students/{student.id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Student not found"})


if __name__ == "__main__":
    unittest.main()
