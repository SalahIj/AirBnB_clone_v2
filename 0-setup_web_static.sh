#!/usr/bin/env bash
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default


# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart

exit 0
