@echo off

cd /d C:\Program Files\MySQL\MySQL Server 5.7\bin

mysqldump -uroot -p123456 --databases learn > %~dp0\learn_databaseBackup.sql

pause