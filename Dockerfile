# Use a base image
FROM ubuntu:latest

# Set the working directory
RUN apt-get update && \
    apt-get install rpm

# Clean package cache to reduce image size
RUN apt-get clean

# Copy the application code into the container

CMD ["rpm tool"]

