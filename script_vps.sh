#!/bin/bash

cd ..
sudo su # Dans le root ou pas ?

#Changement de port
sed -i "s/^Port.*/Port /" /etc/ssh/sshd_config
systemctl restart sshd.service

exit

sudo apt-get update

# Install fail2ban + Config
sudo apt-get install fail2ban


sed -i "s/^findtime.*/findtime = 600/" /etc/fail2ban/jail.conf
sed -i "s/^maxretry.*/maxretry = 3/" /etc/fail2ban/jail.conf


# Modif IpTables
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 22222 -j ACCEPT
iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -P INPUT DROP


# Install Docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


cd web-todos/
sudo chmod +x /usr/local/bin/docker-compose;
docker-compose up --build