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
    make run
