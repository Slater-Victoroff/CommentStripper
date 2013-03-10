#this is my initial idea for how to specify the comment syntax for each language
#this will allow us to look up in the dictionary by file extension
#feedback is welcome
import re

class CommentDef:
    def __init__(self, block_regex, line_regex):
        self.blockRegex = blockRegex
        self.lineRegex = lineRegex
        
class CommentDictionary:	
	def __init__(self):
		cstyle = CommentDef('/\*(.|\r|\n)*?\*/', '([/]{2})(.*)')
		python = CommentDef('([\']{3})([.|\r|\n]*?)([\']{3})', '(#)+(.*)')
		perl = CommentDef('(=begin)([.|\r|\n]*?)(=cut)', '(#)+(.*)')
		ruby = CommentDef('(=begin)([.|\r|\n]*?)(=end)', '(#)+(.*)')
		lisp = CommentDef('(#|)([.|\r|\n]*?)(|#)', '(;)+(.*)')
		text = CommentDef('', '')

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
