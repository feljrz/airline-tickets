import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = "sqlite:///" + os.path.join(basedir, "passagens.db")

import os
import sys

# print(sys.path)
