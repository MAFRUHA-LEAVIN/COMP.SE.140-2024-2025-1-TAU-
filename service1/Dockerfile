# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install the required system packages to enable ps, uptime, and other utilities
RUN apt-get update && apt-get install -y procps

# Copy everything from the current directory to /app in the container
COPY . .

# Install the required Python libraries
RUN pip install flask requests

# Expose port 8199 for HTTP server
EXPOSE 8199

# Run the service1.py when the container starts
CMD ["python", "service1.py"]
