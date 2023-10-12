#!/usr/bin/bash

while true
do
  if wget --server-response --spider $1
  then
    echo done
    paplay $BEEP
    exit 0
  else
    echo false
    paplay $BEEP
  fi
  sleep 1
done
