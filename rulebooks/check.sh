#!/usr/bin/bash

CONFIG_PATH='/etc/hosts'
PREV_DIGEST='498f494232085ec83303a2bc6f04bea840c2b210fbbeda31a46a6e5674d4fc0e'

while [ true ]; do

  DIGEST=$(sha256sum $CONFIG_PATH | awk '{print $1}')
  if [ $PREV_DIGEST = $DIGEST ]; then
    echo "equal"
    sleep 3
  else
    echo "not equal"
    curl -H 'Content-Type: application/json' -d "{\"message\": \"/etc/hosts is modified\"}" 10.9.92.12:5000/endpoint
    sleep 30
  fi

done
