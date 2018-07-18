#!/bin/bash
yes | sudo apt-get update
yes | sudo apt-get upgrade
yes | sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
yes | curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
yes | sudo apt-get install docker-ce
sudo docker-compose build
sudo docker-compose up 