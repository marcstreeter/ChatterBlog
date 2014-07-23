# -*- mode: ruby -*-
# vi: set ft=ruby :

$bash_provision = <<EOF
echo "BLAARG!"
yum -y install http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-release-1.0-11.ius.centos6.noarch.rpm http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/epel-release-6-5.noarch.rpm
yum -y install mysql-server python27 python27-pip python27-tools python27-devel vim-enhanced mysql-devel curl wget
pip2.7 install -r /var/www/chatterblog/requirements.txt
# pip2.7 uninstall simplifycommerce-sdk-python -y
# cd /usr/src; wget -O simplifycommerce-sdk-python-1.1.2.tgz https://www.simplify.com/commerce/static/sdk/python/simplifycommerce-sdk-python-1.1.2.tgz
# tar xzf simplifycommerce-sdk-python-1.1.2.tgz
# cd simplifycommerce-sdk-python-1.1.2
python2.7 setup.py install
chkconfig mysqld on
service mysqld start
mysql -uroot -e 'GRANT ALL PRIVILEGES ON *.* TO "chatterblog"@"localhost" IDENTIFIED BY "UrNotAG04t"; FLUSH PRIVILEGES';
mysql -uroot -e 'DROP DATABASE IF EXISTS chatterblog; CREATE DATABASE chatterblog;'
echo "Populating random data"
cd /var/www/chatterblog/app/
# /usr/bin/python2.7 /var/www/chatterblog/app/generate_data.py
#rm -fv /etc/nginx/conf.d/default.conf
#cp -v /var/www/chatterblog/nginx.conf /etc/nginx/conf.d/chatterblog.conf
#mkdir -pv /var/log/uwsgi/ /etc/supervisord.d
#cp -v /var/www/chatterblog/etc_supervisord.conf /etc/supervisord.conf
#cp -v /var/www/chatterblog/supervisord.conf /etc/supervisord.d/chatterblog.conf
cp -fv /var/www/chatterblog/upstart.conf /etc/init/chatterblog.conf
service iptables stop;chkconfig iptables off
stop chatterblog
start chatterblog
EOF

Vagrant.configure("2") do |config|
  config.vm.box_url = ""
  config.vm.define :chat do |chat|
  chat.vm.box = "centos-64-x64"
  chat.vm.box_url = "http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20131103.box"
  chat.vm.network :private_network, ip: "192.168.200.18"
  chat.vm.hostname = "dev.chatter.chat"
  chat.vm.synced_folder ".", "/var/www/chatterblog"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  chat.vm.provision :shell, inline: $bash_provision
  end
end
