import sys
import re

#Global variables for input html files
file = sys.argv[1]

def minify(file):	
	#Read in file and remove line breaks and tabs
	with open(file, 'r+') as i:
		lines = i.read()
		lines = re.sub("\n", "", lines)
		lines = re.sub("	", "", lines)
		i.seek(0)
		i.write(lines)
		i.truncate()
	i.closed

if __name__ == '__main__':
	#Run Function
	minify(file)