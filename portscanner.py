#!/bin/python3
import sys
import socket 
from datetime import datetime
#define our targer
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("Invalid amount of argument")
	print("syntex error:python3 scanner.py <ip>")	
	
#Add pretty banner 
print('-'*50)
print("scanning target:"+target)
print("Time stated:"+ str(datetime.now()))
print('-'*50)

try:
	for port in range(50,85):
	  s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	  socket.setdefaulttimeout(1)
	  result = s.connect_ex((target,port))
	  if result == 0:
	  	print(f"Port {port} is open")
	  	
except KeyboardInterrupt:
	print("\n Exisiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("COult not connect to host")
	sys.exit()
	
