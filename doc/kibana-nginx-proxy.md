# Set up Kibana Nginx Reverse Proxy

## Create a self-signed certificate or get one from Lets Encrypt
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
```

## Install Nginx
```bash
sudo apt install nginx
```

## Create htpasswd users
```bash
sudo sh -c "echo -n 'usernamehere:' >> /etc/nginx/.htpasswd"
sudo sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"
sudo nano /etc/nginx/.htpasswd 
```

## Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/kibana
```

### Nginx Configuration
```bash
server {
  listen 80;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name servernamehere;
  ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
  ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

  location / {
    proxy_pass http://localhost:5601;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-NginX-Proxy true;
    auth_basic "Restricted Content";
    auth_basic_user_file /etc/nginx/.htpasswd;

    # Enables WS support
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_redirect off;
  }
}

```

### Change Kibana Config
Set server.host directive to "localhost"

Restart Kibana.
```bash
sudo service kibana stop
sudo service kibana start
```

Link Nginx Kibana config and restart Nginx.
```bash
sudo ln -s /etc/nginx/sites-available/kibana /etc/nginx/sites-enabled/kibana
 
sudo systemctl enable nginx.service
sudo systemctl restart nginx.service
```

