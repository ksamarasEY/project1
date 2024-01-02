# Using a base image with Python installed
FROM python:3.8-slim

# Set a working directory
WORKDIR /app

# Copy everything from the current directory (your Python application) to the working directory in the Docker image
COPY . /app

# Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Run your Python script (replace app.py with your script name)
CMD [ "python", "./app.py" ]
