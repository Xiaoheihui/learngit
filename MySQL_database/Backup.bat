@echo off

cd /d D:\Program Files (x86)\mysql-8.0.17-winx64\bin

mysqldump -uroot -p123456 --databases learn > %~dp0\learn_databaseBackup.sql

pause