# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Run the Python script when the container starts
CMD ["python", "app.py"]  # Change "app.py" to your actual script name
