print('test')

import os

dir = 'c:\\'
for f in os.listdir(dir):
    if os.path.isdir(os.path.join(dir, f)):
        print(f)