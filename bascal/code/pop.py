#pop.py
import sys
from poplib import POP3
import socket
from getpass import getpass

#pop3 server
POP3SVR='pop3.qq.com'
print("enter the emali:")
username = input()
password = getpass("enter the password")
try:
	recvSvr = POP3(POP3SVR)
	recvSvr.user(username)
	recvSvr.pass_(password)

	ret = recvSvr.stat()
	print(ret)
	#exit
	recvSvr.quit()
except(socket.gailerror,socket.error,socket.herror) as e:
	print(e)
	sys.exit(1)