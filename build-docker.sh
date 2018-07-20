#!/bin/sh
sudo gpasswd -a $(whoami) docker
sudo chgrp docker /var/run/docker.sock
cd nginx-proxy
sudo docker-compose build
cd ../homepage
sudo docker-compose build