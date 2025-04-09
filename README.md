🎓 Student CRUD REST API
A simple RESTful API to manage students, built with Python (Flask) and deployed using Docker, NGINX, and Vagrant for local production-like setup.

🔧 Features
Full CRUD support for student records

PostgreSQL database

REST API versioning (/api/v1/)

Load-balanced API using NGINX

Configurable with environment variables

Unit testing and linting support

Postman collection for API testing

CI/CD pipeline with Docker image build and push

📁 Project Structure
.
├── app/                  # Flask application
├── nginx/                # NGINX configuration
├── tests/                # Unit tests
├── Dockerfile            # Multi-stage API build
├── docker-compose.yml    # Compose services
├── Makefile              # Project commands
├── Vagrantfile           # VM config for local prod
├── provision.sh          # VM setup script
└── README.md

🚀 Local Development
▶️ Prerequisites
Python 3.9+

Docker + Docker Compose

Vagrant + VirtualBox

Postman (for testing)

🐳 Docker Setup (Without Vagrant)
# Build and start containers
make build
make up

# Stop services
make down

🖥️ Vagrant Production-Like Environment
This sets up a VM and runs the API in Docker containers inside it.

✅ Steps
# Start Vagrant box and deploy services
vagrant up

# SSH into the VM if needed
vagrant ssh

# The API will be accessible via:
http://localhost:8080/api/v1/healthcheck
🔁 API Load Balancing
Two API containers: api1, api2

Managed by NGINX via nginx/nginx.conf

Load balanced via round-robin strategy

Access via: http://localhost:8080/api/v1/students

📫 Using Postman
Use the provided Postman collection to:

✅ GET all students

✅ POST a new student

✅ PUT update student details

✅ DELETE a student

✅ /healthcheck endpoint

🧪 Run Tests
make test

✅ Lint the Code
make lint

🐋 Docker Image Tags
Images are tagged using semantic versioning

Avoids use of latest tag

🔐 Environment Variables
Environment variables like DATABASE_URL are passed dynamically.

To override:

docker run --env DATABASE_URL=... ...
⚙️ CI/CD Workflow
A GitHub Actions pipeline handles:

Build

Test

Lint

Docker build & push

Only runs on changes to app/, Dockerfile, or Makefile, and can be manually triggered.

👷‍♂️ Self-Hosted Runner Setup
Install GitHub self-hosted runner on your local machine to use the pipeline efficiently.

📦 Docker Registry (Optional)
Make sure to configure the following GitHub Secrets:

DOCKER_USERNAME

DOCKER_PASSWORD

👏 Contributors
Built by [Your Name] — Powered by Python, Flask, Docker, and Vagrant 🚀