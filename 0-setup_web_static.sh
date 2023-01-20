#!/usr/bin/env bash
sudo ldconfig -p | grep nginx

if [ "$?" -eq 0 ]
then
	sudo apt update
	sudo apt -y install nginx
	sudo service nginx start
fi

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current
echo "The NGINX SOFTWARE installed successfully!!" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER" /data/
sudo chown "$USER" /etc/nginx/sites-enabled/default
sudo echo -e "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\tlocation / {\n\t\troot /data/web_static/releases/test/;\n\t}\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n}" > /etc/nginx/sites-enabled/default
sudo service nginx restart
