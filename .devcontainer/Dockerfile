# Use an official Python runtime as the base image
FROM python:3.11

# Expose the port you Flask app will run on
EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY ../src /app/src

# Define the command to run your app
CMD ["python", "src.pkr.py"]
