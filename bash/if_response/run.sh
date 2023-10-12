#!/usr/bin/bash

# Waiting a link to response, and 

while true
do
  SECONDS=0
  if wget --server-response --spider $1
  then
    if [ $SECONDS -lt 5 ]; then
      echo done
      for i in {1..5}; do
        paplay $BEEP
      done
      exit 0
    fi
  else
    echo false
  fi
  sleep 1
done
