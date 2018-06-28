## Installing Elasticsearch, Kibana and Logstash

﻿Update your ubuntu installation.
```bash
sudo apt update && sudo apt -y upgrade && sudo apt dist-upgrade && sudo apt clean && sudo apt autoclean && sudo apt -y autoremove
# Install apt-transport-https
sudo apt install apt-transport-https
```

### Install Oracle Java 8 JDK
```bash
# Add Oracle 8 PPA
sudo apt-add-repository ppa:webupd8team/java
# Install Oracle Java 8 JDK
sudo apt install oracle-java8-installer oracle-java8-set-default
```

### Install the Elastic stack
```bash
# Download and install the public key:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
# Save the repository list
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
sudo apt update
# Install the elastic stack
sudo apt install elasticsearch kibana logstash
```
Enable and start the services.
```bash
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
sudo systemctl start kibana.service
```
Check whether the services are running
```bash
curl -X GET "localhost:9200/"
```
You should see some JSON output ending with *"You Know, for Search"*. Also, you can check the service status using:
```bash
sudo service elasticsearch status
sudo service kibana status
```
