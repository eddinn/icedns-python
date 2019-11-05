#!/usr/bin/env python3
import socket
import sys

# Author:   Edvin Dunaway
# Email:    edvin@eddinn.net
# Version:  0.1.2
# Licence:  MIT

# Don't do anything, return Usage and exit if we are missing
# the arg or args are more than one.
if len(sys.argv) != 2:
    print('Usage: icedns.py <ipaddress>')
    exit(1)

# Get the IP from argv
ip = sys.argv[1]


# Define the funtion to look up the reversed IP
def lookup():
    # Reverse the IP and append the arpa host
    revip = '.'.join(reversed(ip.split('.'))) + '.iceland.rix.is'
    # Try for the local resolve and return true if True
    try:
        if socket.gethostbyname(revip) == '127.1.0.1':
            print(ip, 'is an .is IP')
            exit(0)
    # Else return False
    except Exception as e:
        print(ip, 'is not an .is IP -', format(e))
        exit(1)


# Run the function with given argv
lookup()
