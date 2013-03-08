class CommentDef:
    def __init__(self, block_regex, line_regex):
        self.block_regex = block_regex
        self.line_regex = line_regex
		
cstyle = CommentDef('/\*(.|\r|\n)*?\*/', '//.*')
python = CommentDef(None, '#.*')

comment_dict = {'c': cstyle, 'cpp': cstyle, 'cs': cstyle,
                'py': python}
