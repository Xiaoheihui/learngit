@echo off

cd /d C:\Program Files\MySQL\MySQL Server 5.7\bin

mysql -uroot -p123456 learn < %~dp0\learn_databaseBackup.sql

pause