@echo off

cd /d D:\Program Files (x86)\mysql-8.0.17-winx64\bin

mysql -uroot -p123456 learn < %~dp0\learn_databaseBackup.sql

pause