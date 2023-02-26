P.s: This commands come handy if there is any permission related issue in docker
sudo chmod 666 /var/run/docker.sock


Run these commands when docker is installed but not the docker-compose
1) sudo curl -L "https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-$(uname -s)-$(uname -m)"  -o /usr/local/bin/docker-compose
2) sudo mv /usr/local/bin/docker-compose /usr/bin/docker-compose
3) sudo chmod +x /usr/bin/docker-compose


For permission
sudo chown -R bilal microservices



Database permission issue
sudo chown -R mysql:mysql /var/lib/mysql/database_name