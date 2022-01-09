#!/bin/bash
# Takes url and passed email as argument
curl -sX POST -d "email=hr@test@gmail.com&subject=I will always be there for PLD" "$1"
