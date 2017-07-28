"""
count number of files in a given folder (path)
"""

import os, os.path
## simple version for working with CWD
def count(path):
    count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    count =str(count)
    print (count)
