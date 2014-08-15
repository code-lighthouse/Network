! /usr/bin/python

import socket

# Shows the Local Machine's Information (Hostname and IP Adress)

host_name = socket.gethostname()

print('Host name: %s' %host_name)
print('IP adress: %s' %socket.gethostbyname(host_name))
