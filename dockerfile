# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose the port that the app will run on
EXPOSE 8000

# Define the command to run the application
# CMD ["gunicorn", "--bind", "127.0.0.1:8000", "NoteApplication.wsgi:application"]
CMD ["gunicorn", "NoteApplication.wsgi:application", "-b", "0.0.0.0:8000"]

