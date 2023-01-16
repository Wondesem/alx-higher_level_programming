#!/bin/bash
# makes a request that causes serves to send "You got me!" as a response
curl -sL -X PUT -H "Origin: ALXSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
