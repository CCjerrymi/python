#file.py

class MyFile:
	#file = ""
	message = 'hello'

	def __init__(self):
	    print('this is the constructor method!!')

	def __del__(self):
		print("object ending!!")

	@classmethod
	def myRead(cls):
		file = open("../txt/temp.txt")
		print(cls.message)
		while True:
			chunck = file.read(10)
			if not chunck:
				break
			print(chunck)

myfile = MyFile()
myfile.myRead()
	


