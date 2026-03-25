FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies including those required for pyttsx3 (espeak) and psycopg2 (libpq-dev)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    espeak \
    libespeak1 \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port 8000 for the Azure Container App
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PROJECT.wsgi:application"]
