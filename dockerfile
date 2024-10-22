FROM ubuntu:18.04

# Insecure: Using an outdated base image
RUN apt-get update && apt-get install -y openssl

# Insecure: Running as root
USER root
