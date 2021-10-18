import os, shutil

listOfFiles = [] 
with open(r'example\Desktop\list.txt') as listDocument:
    for row in listDocument:
        listOfFiles.append(row)

for root, dirs, files in os.walk(r'\\example\directory\images\old'):
    for _file in files:
        if _file + '\n' in listOfFiles:
            print
            'Found file in: ' + str(root)
            shutil.copy(os.path.abspath(root + '/' +  _file), r'\\example\directory\images\new')
        else:
            print ("file: {}".format(_file))
