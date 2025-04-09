#!/bin/bash

install_docker() {
  echo "Installing Docker..."
  curl -fsSL https://get.docker.com -o get-docker.sh
  sh get-docker.sh
}

install_docker_compose() {
  echo "Installing Docker Compose..."
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
}

setup_project() {
  echo "Spinning up services with Docker Compose..."
  cd /vagrant
  docker-compose up -d
}

main() {
  install_docker
  install_docker_compose
  setup_project
}

main
