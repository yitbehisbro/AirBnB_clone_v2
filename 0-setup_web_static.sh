#!/usr/bin/env bash
#Configurations for ngnix to deploy AirBnB project
sudo apt update
sudo apt -y install nginx
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# sudo mkdir -p /data/web_static/current
sudo touch /data/web_static/releases/test/index.html
sudo chown "$USER" /data/web_static/releases/test/index.html
sudo echo "The NGINX SOFTWARE installed successfully!!" | sudo tee -i /data/web_static/releases/test/index.html > /dev/null > 2>&1
# sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "ubuntu" /data/
sudo chown "$USER" /etc/nginx/sites-enabled/default
sudo echo -e "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\tlocation / {\n\t\troot /data/web_static/releases/test/;\n\t}\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n}" | sudo tee -i /etc/nginx/sites-enabled/default > /dev/null 2>&1
sudo service nginx restart
