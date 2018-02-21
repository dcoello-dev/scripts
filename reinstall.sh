sudo apt-get install -y chromium-browser nmap ssh vsftpd python-pip apt-transport-https mongodb-server git curl
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install -y sublime-text
sudo apt-get install -y nodejs-legacy npm
sudo pip install flask pymongo requests netifaces websocket paho-mqtt configparser websocket-client 
sudo apt install -y compizconfig-settings-manager htop unity-tweak-tool
