#this is my initial idea for how to specify the comment syntax for each language
#this will allow us to look up in the dictionary by file extension
#feedback is welcome

class CommentDef:
    def __init__(self, block_regex, line_regex):
        self.block_regex = block_regex
        self.line_regex = line_regex
		
cstyle = CommentDef('/\*(.|\r|\n)*?\*/', '([/]{2})(.*)')
python = CommentDef('([\']{3})([.|\r|\n]*?)([\']{3})', '#.*')
perl = CommentDef('(=begin)([.|\r|\n]*?)(=cut)', '#.*')
ruby = CommentDef('(=begin)([.|\r|\n]*?)(=end)', '#.*'

comment_dict = {'c': cstyle, 'cpp': cstyle, 'cs': cstyle,
				'java': cstyle, 'js': cstyle, 'py': python, 
				'pl': perl, 'rb': ruby}
