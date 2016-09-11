import sys
import re
import os

#Global variables for input html files
mode = sys.argv[1]
arg = sys.argv[2]

class Minify:
	def __init__(self):
		print "Minification started!"

	def mode(self, mode, arg):
		if mode == 'd':
			self.minify_directory(arg)
		elif mode == 'f':
			self.minify_file(arg)
		else:
			print "Please specify mode"
		return

	def minify_directory(self, directory):	
		#Read in files and remove line breaks and tabs
		for f in os.listdir(directory):
			file = directory + '/' + f
			with open(file, 'r+') as i:
				lines = i.read()
				lines = re.sub("\n", "", lines)
				lines = re.sub("	", "", lines)
				i.seek(0)
				i.write(lines)
				i.truncate()
			i.closed
		print 'File directory minification complete!'

	def minify_file(self, file):
		with open(file, 'r+') as i:
			lines = i.read()
			lines = re.sub("\n", "", lines)
			lines = re.sub("	", "", lines)
			i.seek(0)
			i.write(lines)
			i.truncate()
		i.closed
		print 'File minification complete!'

if __name__ == '__main__':
	#Run Function
	m = Minify()
	m.mode(mode, arg)