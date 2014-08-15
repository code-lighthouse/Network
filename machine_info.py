#! /usr/bin/python

import socket

# Shows the Local Machine's Information (Hostname and IP Adress)

def print_machine_info():
    host_name = socket.gethostname()
    ip_adress = socket.gethostbyname(host_name)
    print('Host name: %s' %host_name)
    print('IP adress: %s' %ip_adress)

if __name__ == '__main__':
    print_machine_info()
