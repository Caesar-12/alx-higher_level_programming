#!/bin/bash
# Receives a URL, sends a request to the url and
# displays the size of the body of the response

curl -Is "$1" | grep "Content-Length" | cut -d " " -f 2
