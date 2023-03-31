#!/bin/bash
# Displays status code #curl -I -s "$1" | grep "HTTP" | cut -d " " -f 2
curl -o /dev/null -s -w "%{http_code}" "$1"
