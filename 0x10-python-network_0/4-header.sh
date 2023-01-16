#!/bin/bash
# This script applys get and displays the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
