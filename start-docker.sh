#!/bin/sh
yes | docker network create --driver bridge common_link
cd nginx-proxy
sudo docker-compose up -d
cd ../homepage
sudo docker-compose up -d