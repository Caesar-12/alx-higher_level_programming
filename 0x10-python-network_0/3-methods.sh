#!/bin/bash
# Shows allowed options
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
