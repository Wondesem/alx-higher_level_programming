#!/bin/bash
# Sends sends a request to that URL by taking
# URL as input and displays the size of the body of the response
curl -s I "$1" | grep Content-Length: | cut -d ' ' -f 2
