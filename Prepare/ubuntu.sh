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
sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker-compose build
sudo docker-compose up 