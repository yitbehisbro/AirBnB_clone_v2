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
sudo mkdir -p /data/web_static/current
echo "The NGINX SOFTWARE installed successfully!!" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R "$USER" /data/
sudo chown "$USER" /etc/nginx/sites-enabled/default
echo -e "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\tlocation / {\n\t\troot /data/web_static/releases/test/;\n\t}\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n}" | sudo tee /etc/nginx/sites-enabled/default
sudo service nginx restart
