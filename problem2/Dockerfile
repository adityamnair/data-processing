# Use an appropriate base image for Apache Spark
FROM bitnami/spark:3.1.2

# Set the working directory
WORKDIR /app

# Copy the Python script and input CSV file into the container
COPY anonymize_spark.py .
COPY input.csv .

# Copy requirements.txt and install dependencies if needed
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Command to run the Python script with Spark
CMD ["spark-submit", "--master", "local[*]", "anonymize_spark.py"]
