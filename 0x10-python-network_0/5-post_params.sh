#!/bin/bash
# Takes url and passed email as argument
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
