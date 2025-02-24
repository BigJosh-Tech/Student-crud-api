import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///students.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database and logger
db = SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)

# Models


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)


# Seed initial data


def seed_data():
    students = [
        {"id": 1, "name": "Joshua", "age": 22, "grade": "A"},
        {"id": 2, "name": "Femi", "age": 25, "grade": "B1"},
        {"id": 3, "name": "Clark", "age": 29, "grade": "B2"},
    ]

    for student in students:
        existing_student = Student.query.get(student["id"])
        if not existing_student:
            new_student = Student(
                id=student["id"],
                name=student["name"],
                age=student["age"],
                grade=student["grade"],
            )
            db.session.add(new_student)
    db.session.commit()
    logging.info("Initial student data seeded.")


# Routes


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/v1/students", methods=["POST"])
def create_student():
    try:
        data = request.get_json()
        logging.info(f"Received data: {data}")

        if not data:
            logging.error("No JSON data provided.")
            return jsonify({"error": "No JSON data provided"}), 400

        required_fields = ["name", "age", "grade"]
        missing_fields = [
            field for field in required_fields if field not in data
        ]
        if missing_fields:
            logging.error(f"Missing fields: {missing_fields}")
            return (
                jsonify({
                    "error": f"Missing fields: {', '.join(missing_fields)}"
                }),
            )

        student = Student(
            name=data["name"], 
            age=data["age"], 
            grade=data["grade"]
        )

        try:
            db.session.add(student)
            db.session.commit()
            logging.info(f"Student created: {student}")
            return (
                jsonify(
                    {
                        "id": student.id,
                        "name": student.name,
                        "age": student.age,
                        "grade": student.grade,
                    }
                ),
                201,
            )
        except Exception as e:
            logging.error(f"Database error: {e}")
            db.session.rollback()
            return jsonify({"error": "Internal server error"}), 503
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/v1/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return (
        jsonify(
            [
                {"id": s.id, "name": s.name, "age": s.age, "grade": s.grade}
                for s in students
            ]
        ),
        200,
    )


@app.route("/api/v1/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        logging.warning(f"Student not found: {student_id}")
        return jsonify({"error": "Student not found"}), 404
    return (
        jsonify(
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "grade": student.grade,
            }
        ),
        200,
    )


@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    student = Student.query.get(student_id)
    if not student:
        logging.warning(f"Student not found: {student_id}")
        return jsonify({"error": "Student not found"}), 404

    student.name = data.get("name", student.name)
    student.age = data.get("age", student.age)
    student.grade = data.get("grade", student.grade)
    db.session.commit()
    logging.info(f"Student updated: {student}")
    return (
        jsonify(
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "grade": student.grade,
            }
        ),
        200,
    )


@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        logging.warning(f"Student not found: {student_id}")
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()
    logging.info(f"Student deleted: {student_id}")
    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
    # Bind the Flask app to 0.0.0.0 so it's accessible from outside the
    # container
    app.run(host="0.0.0.0", port=5000, debug=True)
