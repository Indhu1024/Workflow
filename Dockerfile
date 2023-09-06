# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y curl python3-pip && \
    pip3 install sarif-tools

# Clean up package cache to reduce image size
RUN apt-get clean

# Set the SARIF tools as the default command when running the container
CMD ["sarif"]

