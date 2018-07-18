yes | sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
yes | sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yes | sudo yum-config-manager --enable docker-ce-edge
yes | sudo yum install docker-ce
sudo docker-compose build
sudo docker-compose up 