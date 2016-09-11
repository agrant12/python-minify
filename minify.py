import sys, re, os

#Global mode and directory/file path
mode = sys.argv[1]
path = sys.argv[2]

class Minify:
	def __init__(self):
		print "Minification started!"

	def mode(self, mode, path):
		if mode == 'd':
			self.minify_directory(path)
		elif mode == 'f':
			self.minify_file(path)
		else:
			return self.error("Incorrect mode param! Please use 'd' for directory minification or 'f' for single file minification.")
		return

	def minify_directory(self, directory):	
		#Read in files within directory and remove line breaks and tabs
		if os.path.isdir(directory):
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
		else:
			return self.error('Not a directory! Please enter directory path.')
		
		print 'File directory minification complete!'

	def minify_file(self, file):
		#Read in file and remove line breaks and tabs
		if os.path.isfile(file):
			with open(file, 'r+') as i:
				lines = i.read()
				lines = re.sub("\n", "", lines)
				lines = re.sub("	", "", lines)
				i.seek(0)
				i.write(lines)
				i.truncate()
			i.closed
		else:
			return self.error('Not a file! Please enter a file path.')
		
		print 'File minification complete!'

	def error(self, err):
		#Print error message
		print err

if __name__ == '__main__':
	#Run Function
	m = Minify()
	m.mode(mode, path)