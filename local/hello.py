import os
import re

if not os.path.exists('test.txt'):
    os.system('touch test.txt')
    print('success to creat testfile !')

else:
    print('testfile has exists !')