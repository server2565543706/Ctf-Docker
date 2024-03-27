#!/bin/bash
set -e

echo  -e "flag=\"$GZCTF_FLAG\""  > /usr/src/app/flag.py

export GZCTF_FLAG=not_flag
GZCTF_FLAG=not_flag

while test "1" = "1"
do
sleep 1000
done
