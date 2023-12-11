FROM python:3.10

# Install any necessary dependencies
# Copy your Python script into the container
COPY anycloud/aws/batch/calculate_primes.py /app/calculate_primes.py

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["python3.10", "calculate_primes.py"]
