import os
def search(x, dir):
    for thing in os.scandir(dir):
        newpath=os.path.join(dir, thing.name)
        if os.path.isfile(thing):
            if x in thing.name:
                print(os.path.relpath(newpath, a)) #global
        elif os.path.isdir(thing):
            search(x, newpath)

a=os.getcwd()
b=input('please input what you want to find:')
search(b,a)

'''
import os.path

pfile = os.walk('.')

file_list = []

for dirpath, dirnames, filenames in pfile:
    for name in filenames:
        if ".py" in name:
            file_list.append(dirpath+'\'+name)

for file_g in file_list:
    print(file_g)
'''    
