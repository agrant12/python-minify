import sys, re, os
from message import messages

#Global mode and directory/file path
mode = sys.argv[1]
path = sys.argv[2]

class Minify:

	def __init__(self):
		print messages["start"]

	def mode(self, mode, path):
		if mode == 'd':
			self.directory(path)
		elif mode == 'f':
			self.file(path)
		else:
			self.error(messages["error_mode"])

	def directory(self, directory):
		if os.path.isdir(directory):
			for f in os.listdir(directory):
				file = directory + '/' + f
				self.minify(file, file + ' ' + messages["file_directory"])
		else:
			self.error(messages['error_directory'])

	def file(self, file):
		if os.path.isfile(file):
			self.minify(file, file + ' ' + messages["file_complete"])
		else:
			self.error(messages['error_file'])

	def minify(self, path, message):
		with open(path, 'r+') as i:
			lines = i.read()
			lines = re.sub("\n", "", lines)
			lines = re.sub("	", "", lines)
			i.seek(0)
			i.write(lines)
			i.truncate()
		i.closed
		print message

	def error(self, err):
		#Print error message
		print err

if __name__ == '__main__':
	#Run Function
	m = Minify()
	m.mode(mode, path)