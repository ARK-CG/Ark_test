#!/bin/sh
yes | network create --driver bridge shared
cd nginx-proxy
sudo docker-compose up
cd ../homepage
sudo docker-compose up