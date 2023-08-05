# Use an appropriate base image (Python 3.9)
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port for the Django development server
EXPOSE 8000

# Run tests
RUN python manage.py test

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
