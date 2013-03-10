#this is my initial idea for how to specify the comment syntax for each language
#this will allow us to look up in the dictionary by file extension
#feedback is welcome
import re

class CommentDef:
    def __init__(self, blockRegex, lineRegex, blockContinuation=""):
        self.blockRegex = blockRegex
        self.lineRegex = lineRegex
        self.blockContinuation = blockContinuation
        
class CommentDictionary:	
	def __init__(self):
		cstyle = CommentDef('(/\*)(.|\r|\n)*?(?=(\*/))', '([/]{2})(.*)', "*")
		python = CommentDef('([\']{3})([.|\r|\n]*?)(?=([\']{3}))', '(#)+(.*)')
		perl = CommentDef('(=begin)([.|\r|\n]*?)(?=(=cut))', '(#)+(.*)')
		ruby = CommentDef('(=begin)([.|\r|\n]*?)(?=(=end))', '(#)+(.*)')
		lisp = CommentDef('(#|)([.|\r|\n]*?)(?=(|#))', '(;)+(.*)')
		text = CommentDef('', '')
		#All block comment should be indicated such that the closing
		#element of the comment is in a lookahead assertion to allow
		#for nested comments

		self.reference = {'c': cstyle, 'cpp': cstyle, 'cs': cstyle,
						'java': cstyle, 'js': cstyle, 'py': python, 
						'pl': perl, 'rb': ruby, 'lisp': lisp, 'scm': lisp,
						'txt': text}
						
	def parseInline(self, fileMappings):
		'''Assumes input is the result of the mapFilesToTypes method in
		cli.py. So long as there's a dictionary mapping file paths to file
		types it should be fine though. Returns all supported inline comments'''
		allComments = []
		for key in fileMappings:
			if fileMappings[key] in self.reference:
				regexPattern = self.reference[key].lineRegex
				with open(key, 'r') as corpus:
					for line in corpus:
						if re.match(regexPattern, line):
							allComments.append(re.match(regexPattern, line).group(2))
		return allComments
		
	def parseBlock(self, fileMappings):
		'''Similar to parseInline, except this round looks for block comments'''
		allComments = []
		for key in fileMappings:
			if fileMappings[key] in self.reference:
				regexPattern = self.reference[key].blockRegex
				with open(key, 'r').read() as corpus:
					results = re.finditer(regexPattern, corpus)
					for result in results:
						cleanedResult = []
						result = result.group(2).split('\n')
						for line in result:
							cleanedResult.append(line.strip()[len(self.reference[key].blockContinuation):].lower())
						allComments.append(" ".join(cleanedResult))
		return allComments
					
