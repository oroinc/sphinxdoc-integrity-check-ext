import os
import sys

sys.path.append(os.path.abspath("./../"))

master_doc = 'index'

extensions = ['todo', 'oro_integrity_check']

todo_include_todos = False
todo_emit_warnings = False
