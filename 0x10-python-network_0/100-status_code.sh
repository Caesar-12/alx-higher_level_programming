#!/bin/bash
# Displays status code #curl -I -s "$1" | grep "HTTP" | cut -d " " -f 2
curl -s -o /dev/null -w "%{http_code}\n" "$1"
