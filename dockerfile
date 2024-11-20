# Base image with a vulnerable version of Ubuntu
FROM ubuntu:14.04

# Install an outdated and vulnerable version of OpenSSL
RUN apt-get update && apt-get install -y openssl=1.0.1-4ubuntu5.39

# Switch to a second stage using a vulnerable version of Nginx
FROM nginx:1.18

# Add a hardcoded weak root password
RUN echo "root:weakpassword" | chpasswd

# Change permissions to 777 on the Nginx configuration file
RUN chmod 777 /etc/nginx/nginx.conf
