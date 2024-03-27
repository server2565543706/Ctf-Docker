#!/bin/sh
# Add your startup script

# DO NOT DELETE
echo $GZCTF_FLAG > /home/ctf/flag
/etc/init.d/xinetd start;
sleep infinity;
