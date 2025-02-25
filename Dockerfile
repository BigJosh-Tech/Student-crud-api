# Stage 1: Build Stage
FROM --platform=linux/amd64 python:3.9-slim AS build

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime Stage
FROM --platform=linux/amd64 python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL="sqlite:////app/data/students.db"

# Create a volume for SQLite database persistence
VOLUME ["/app/data"]

# Set working directory
WORKDIR /app

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Expose application port
EXPOSE 5000

# Set default command to run the API
CMD ["python", "app.py"]
