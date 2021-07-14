import os

NAME = 'samgr'
DESCRIPTION = 'A command line tool to help you manage your shell aliases.'
VERSION = '1.0.0'

AUTHOR = 'IvanEFan'


usr_home = os.path.expanduser('~')
SAMGRRC_PATH = os.path.join(usr_home, '.samgrrc')
ZSHRC_PATH = os.path.join(usr_home, '.zshrc')

