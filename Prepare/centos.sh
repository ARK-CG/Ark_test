yes | sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
yes | sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yes | sudo yum-config-manager --enable docker-ce-edge
yes | sudo yum install docker-ce
sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker-compose build
sudo docker-compose up 