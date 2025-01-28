# Student CRUD API

This project implements a REST API for managing student records.

## Features
- API versioning (`/api/v1/<resource>`)
- CRUD operations for students
- Logs meaningful messages with appropriate log levels
- Supports health check at `/api/v1/healthcheck`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/BigJosh-Tech/Student-crud-api.git
   cd student-crud-api

2. Create a virtual environment and install dependencies:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Set up environment variables: Create a .env file with:
    DATABASE_URL=sqlite:///students.db

4. Run the application:
    python app.py
    The API will be available at: http://127.0.0.1:5000/api/v1/students
    
5. Testing the API with Postman
    Import Postman Collection
    Open Postman.
    Click Import and upload the api.postman_collection.json file from the project.

6. Test API Endpoints
- Healthcheck:
    Use the GET /api/v1/healthcheck request to verify the API is running.
- Get All Students:
    Use the GET /api/v1/students request to view all student records.
- Get a Single Student:
    Use the GET /api/v1/students/<id> request, replacing <id> with a student’s ID (e.g., 1).
- Create a Student:
    Use the POST /api/v1/students request and provide a JSON body.
- Update a Student:
    Use the PUT /api/v1/students/<id> request, replacing <id> with the student ID, and provide updated data in the JSON body.
- Delete a Student:
    Use the DELETE /api/v1/students/<id> request to remove a student by ID.

7. Logging
    Logs are automatically generated for every API action:

# REST API with Flask and Docker

This is a Flask-based REST API for managing students, which is containerized using Docker.

## Prerequisites
- Docker
- Make (optional, but recommended)

## Setup Instructions

### Build Docker Image
Use the following command to build the Docker image for the Student CRUD API:
```bash
docker build -t student-crud-api:1.0.0 .

Replace 1.0.0 with the desired semantic version for the image.

Run the container using the following command:
 docker run -d -p 5000:5000 --env-file .env student-crud-api:1.0.0 

The API will be accessible at http://127.0.0.1:5000/api/v1/students