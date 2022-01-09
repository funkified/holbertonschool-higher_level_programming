#!/bin/bash
# Takes URL as an argument, sends a GET requests UR:, and display body 
curl -sX GET -H "X-School-User-Id: 98" "$1"
