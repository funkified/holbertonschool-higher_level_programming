#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
"""
import urllib.request as req
import urllib.parse
from sys import argv


if __name__ == '__main__':
    email = argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    url = req.Request(argv[1], data)
    with req.urlopen(url) as response:
        print(response.read().decode('utf-8'))
