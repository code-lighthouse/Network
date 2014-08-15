! /usr/bin/python

import socket

host_name = socket.gethostname()

print('Host name: %s' %host_name)
print('IP adress: %s' %socket.gethostbyname(host_name))
