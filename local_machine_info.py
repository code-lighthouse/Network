#! /usr/bin/python

import socket

class LocalMachineInfo(object):
    def __init__(self):
        host_name = socket.gethostname()
        ip_adress = socket.gethostbyname(host_name)
        print('Host name: %s' %host_name)
        print('IP adress: %s' %ip_adress)

if __name__ == '__main__':
    LocalMachineInfo()


