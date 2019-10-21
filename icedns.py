#!/usr/bin/env python3
import sys, ipaddress, socket

# Don't do anything if we are missing the arg or args are more than one
if len(sys.argv) != 2:
  print('Usage: icedns.py <ipaddress>')
  sys.exit(1)

# Get the IP from argv
ip = sys.argv[1]
# Reverse the IP and append the arpa
revip = '.'.join(reversed(ip.split('.'))) + '.iceland.rix.is'
# Try for the local resolve and return True
try:
  if socket.gethostbyname(revip) == '127.1.0.1':
    print(ip, 'is an .is IP')
# Else return False
except:
  print(ip, 'is not an .is IP')
