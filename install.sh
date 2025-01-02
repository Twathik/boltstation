sudo apt update
sudo apt upgrade
sudo apt install add-apt-repository

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl libgirepository1.0-dev libcairo2-dev
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo groupadd docker

newgrp docker

docker run hello-world

sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R

sudo systemctl enable docker.service
sudo systemctl enable containerd.service

mokutil --sb-state

sudo add-apt-repository "deb http://deb.debian.org/debian/ bookworm main contrib non-free non-free-firmware"

sudo apt update
sudo apt install nvidia-driver firmware-misc-nonfree

curl -fsSL https://ollama.com/install.sh | sh

docker compose up -d

sh ./setup.sh

docker exec -it keycloak bash -c "/opt/keycloak/bin/kcadm.sh config credentials --server http://localhost:8080 --realm master --user admin --password admin ; /opt/keycloak/bin/kcadm.sh update realms/master -s sslRequired=NONE;"

curl -fsSL https://tailscale.com/install.sh | sh
tailscale up



