sudo dnf install -y mariadb105-server 
sudo systemctl start mariadb 
sudo systemctl enable mariadb 
nano /etc/my.cnf.d/mariadb-server.cnf 

[mysqld] 
port=63306
 [galera] 
bind-address=0.0.0.0 

sudo systemctl restart mariadb



CREATE USER 'synan'@'%' IDENTIFIED BY 'haydegidelum';
GRANT ALL PRIVILEGES ON *.* TO 'synan'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
