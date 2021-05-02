import os as os
maindir = 'S3E34'
list = os.listdir(maindir)
for name in list:
    skrypt = open(maindir+"//"+name)
    exec(skrypt.read())