#!/bin/bash
# Display all http methods the server accepts
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
