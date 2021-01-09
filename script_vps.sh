#!/bin/bash

cd ..

#Changement de port
sudo sed -i "s/^Port.*/Port 2222/" /etc/ssh/sshd_config
sudo systemctl restart sshd.service

sudo apt-get update

# Install fail2ban + Config
sudo apt-get install fail2ban
sudo sed -i "s/^findtime.*/findtime = 600/" /etc/fail2ban/jail.conf
sudo sed -i "s/^maxretry.*/maxretry = 3/" /etc/fail2ban/jail.conf


# Modif IpTables
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22222 -j ACCEPT
sudo iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP


# Install Docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


cd web-todos/
sudo chmod +x /usr/local/bin/docker-compose;
docker-compose up --build