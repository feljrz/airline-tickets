import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir,'passagens.db')

import sys, os
# print(sys.path)
