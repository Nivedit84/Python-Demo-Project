# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install flask

# Run the Flask app
CMD ["python", "app.py"]
