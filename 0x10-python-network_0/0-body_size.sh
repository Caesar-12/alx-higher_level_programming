#!/bin/bash
# Receives a URL, sends a request to the url and
curl -Is "$1" | grep "Content-Length" | cut -d " " -f 2
