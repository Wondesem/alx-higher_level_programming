#!/bin/bash
# makes a request that causes serves to send "You got me!" as a response
curl -sLX PUT "You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
