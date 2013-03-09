import sys
import os
import itertools

def parseCommandLineArguments(tagDictionary = {"-r":"recursive"}, allArguments = sys.argv):
	'''For now just allow the recursive tag, and assume every passed
	directory should have the tag. Recursive should be -r.
	Tags should be passed in the form of a dictionary mapping tag
	with meaning. Output of this method should be a dictionary mapping all
	filepaths to the results from the tagDictionary. All tags should start
	with a '-' character, and nothing else should'''
	directoryDictionary = {}
	for i in range(1,len(allArguments)):
		if allArguments[i][0] != '-':
			mapping = ""
			for key in tagDictionary:
				try:
					if allArguments[i+1] == key:
						mapping = tagDictionary[key]
				except IndexError:
					#Should only get an index error while checking the
					#last element of the provided arguments
					print "Near The End"
					continue
			directoryDictionary[allArguments[i]] = mapping
	return directoryDictionary

def getFiles(directoryDictionary):
	'''Takes the dictionary of filepaths and tags and returns a list of 
	all files in the associated directories'''
	path = os.path.abspath(__file__).rstrip('cli.py')
	allFiles = []
	for key in directoryDictionary:
		localPath = path + key
		if directoryDictionary[key] == 'recursive':
			for (current,dirs,files) in os.walk(localPath):
				if files != []:
					allFiles.extend(files)
		else:
			for (current,dirs,files) in os.walk(localPath):
				if files != []:
					allFiles.extend(files)
				break

	return allFiles

print getFiles(parseCommandLineArguments(allArguments=["cli.py","..","-r","../.."]))
