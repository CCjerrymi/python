#myEmail.py
import smtplib
import os

def auth_login():
	print('please input your username:')
	username = input()
	password = getpass('please input your password:')

	try:
		s = smtplib.SMTP(server)
		print(s.shlo())
		code = s.ehlo()[0]
		usersesmtp = 1
		if not (200 <= code <= 299):
			usersesntp = 0
			code = s.ehlo()[0]
			if not (200 <= code <= 299):
				raise SMTPHeloError(code,resp)
		if usersesmtp and s.has_extn('size'):
			print(u"max email size" + s.esmtp_features['size'])
			if len(message) > int (s.esmtp_features['size']):
				print('email is to large')
				sys.exit()

		if usersesmtp and s.has_extn('auth'):
			print(u'\r\nuse connected')
			try:
				s.login(username,userpassword)
			except smtplib.SMTPException as e:
				print(u'login failed:',e)
				sys.exit()
		else:
			print(u'server not suport the login!')
		s.sendmail(formaddr,toaddr,message)

	except (socket.gaierror,socket.error,socket.herror,smtplib.SMTPException) as e:
		print("***send success！")
		prnt(e)
		sys.exit(1)
	else:
		print(u'email send sucess')