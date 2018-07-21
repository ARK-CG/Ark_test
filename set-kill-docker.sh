#!/bin/sh
cd nginx-proxy
sudo docker-compose kill -d
cd ../homepage
sudo docker-compose kill -d