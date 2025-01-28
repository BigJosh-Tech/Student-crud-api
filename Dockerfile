# Stage 1: Build Stage
FROM python:3.9-slim AS build

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime Stage
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy application code
WORKDIR /app
COPY . .

# Expose application port
EXPOSE 5000

# Set default command to run the API
CMD ["python", "app.py"]
