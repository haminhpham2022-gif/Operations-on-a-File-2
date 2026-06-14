import os
if os.path.exists("file1.txt"):
    os.remove('file1.txt')
    print('file deleted successfully')
else:
    print('file does not exist')