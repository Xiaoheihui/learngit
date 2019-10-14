@echo off

copy %~dp0\*.sql %~dp0\databaseBackup

cd %~dp0\databaseBackup

set yy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
set hh=%time:~0,2%
set hh=%hh: =0%
set mn=%time:~3,2%
set ss=%time:~6,2%



set filename=%yy%%k%%mm%%k%%dd%%k%%hh%%m%%mn%%m%%ss%

ren "learn_databaseBackup.sql" "%yy%-%mm%-%dd% %hh%%mn%%ss%.sql"

cd /d D:\Program Files (x86)\mysql-8.0.17-winx64\bin

mysqldump -uroot -p123456 --databases learn > %~dp0\learn_databaseBackup.sql

pause