CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypassword';

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE MY_DB;
