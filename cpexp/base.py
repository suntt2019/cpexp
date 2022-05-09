import os

working_dir = os.path.dirname(__file__)
grammar_file = os.path.join(working_dir, 'antlr', 'CPExp.g4')
generated_files = [os.path.join(working_dir, 'antlr', filename) for filename in [
    'CPExpLexer.py', 'CPExpParser.py', 'CPExpListener.py'
]]
