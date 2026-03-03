# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your uptime script into the container
COPY day15_uptime.py .

# Install the requests library inside the container
RUN pip install requests

# Command to run the script when the container starts
CMD ["python", "day15_uptime.py"]