#!/bin/bash
set -e

echo  -e $GZCTF_FLAG > /var/www/html/7e8d426c-65b8-11ee-b44b-525400cfb560.txt

export GZCTF_FLAG=not_flag
GZCTF_FLAG=not_flag

# Apache gets grumpy about PID files pre-existing
rm -f /usr/local/apache2/logs/httpd.pid
apache2ctl start
while test "1" = "1"
do
sleep 1000
done
