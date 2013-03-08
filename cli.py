import sys

def parseCommandLineArguments(tagDictionary = {"-r":"recursive"}):
	'''For now just allow the recursive tag, and assume every passed
	directory should have the tag. Recursive should be -r.
	Tags should be passed in the form of a dictionary mapping tag
	with meaning. Output of this method should be a dictionary mapping all
	filepaths to the results from the tagDictionary. All tags should start
	with a '-' character, and nothing else should'''
	allArguments = sys.argv
	directoryDictionary = {}
	for i in range(0,len(allArguments)):
		if allArguments[i][0] != '-':
			mapping = ""
			for key in tagDictionary:
				if allArguments[i+1] == key:
					mapping = tagDictionary[key]
			directoryDictionary[allArguments[i]] = mapping
	return directoryDictionary
	
