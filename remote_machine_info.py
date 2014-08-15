#! /usr/bin/python

import socket

class RemoteMachineInfo(object):
    def __init__(self, remote_host):
        self.remote_host = remote_host
        try:
            print('IP Adress: %s' %socket.gethostbyname(remote_host))
        except socket.error, err_msg:
            print('%s: %s' %(self.remote_host, err_msg))

if __name__ == '__main__':
    RemoteMachineInfo("www.google.com")
