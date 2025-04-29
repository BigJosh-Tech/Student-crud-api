#!/usr/bin/env bash

# Update system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
sudo apt-get install -y docker.io

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add Vagrant user to Docker group
sudo usermod -aG docker vagrant

# Install Nginx
sudo apt-get install -y nginx
