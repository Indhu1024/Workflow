# # Use a base image
# FROM centos:8 AS rpm-builder
# # Set the working directory
# WORKDIR /app
# # yum update && \
# RUN sed -i -e 's/^mirrorlist/#mirrorlist/g' -e 's/^#baseurl/baseurl/g' /etc/yum.repos.d/CentOS-Base.repo \
#     && sed -i 's/mirror.centos.org/mirror.example.com/' /etc/yum.repos.d/CentOS-Base.repo \
#     && yum clean all
#  RUN yum install -y rpm-build rpmdevtools

# Stage 2: Copy RPMs to an Ubuntu-based image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Copy RPMs from the previous stage
#COPY --from=rpm-builder /app/rpmbuild/RPMS /app/rpms

# ... Add instructions to work with the RPM packages ...

# For example, you can use alien to convert RPMs to DEB packages on the Ubuntu image.
RUN apt-get update && \
    apt-get install -y rpm
   
CMD ["rpm tools"]
