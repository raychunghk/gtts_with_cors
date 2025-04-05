# Use a lightweight Alpine-based Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for gTTS and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on (port 80 as per the gTTS author's version)
EXPOSE 80

# Command to run the application using gunicorn for production
CMD ["gunicorn", "-b=:80", "--access-logfile=-", "main:app"]

#docker build -t gtts:latest .
#docker run -d --name gtts-service -p 80:80 gtts:latest