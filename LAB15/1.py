import os
filepath = r'C:\sandbox\pythonCourse\LAB15\1.py\openfile.txt'
folderpath = r'C:\sandbox\pythonCourse\LAB15'
print(os.path.exists(filepath))
print(os.path.isfile(filepath))
print(os.path.isdir(folderpath))
filecontentread = open(filepath, 'r')
filecontent = filecontentread.read()
print(filecontent)
filecontentwrite = open('write.txt', 'w')
print(filecontentwrite.write('this is the file'))
