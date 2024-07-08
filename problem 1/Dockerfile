# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
# (if any dependencies are required, list them in requirements.txt)
# RUN pip install -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "./parser.py"]
