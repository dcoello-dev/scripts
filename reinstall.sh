sudo apt-get install -y chromium-browser
sudo apt-get install -y nmap ssh vsftpd python-pip
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install -y apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install -y sublime-text
sudo apt-get install -y mysql-server mongodb-server git curl
sudo apt-get install -y nodejs-legacy npm
sudo pip install flask pymongo requests 
sudo apt install -y compizconfig-settings-manager htop
