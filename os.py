import os 
import datetime
name = os.name
#os.chdir("C:\ ")
#dizin = os.listdir()
#os.mkdir("newDirec")
#os.makedirs("newDirec/yeni")
#for dosya in os.listdir():
    #if dosya.endswith('.py'):
        #print(dosya)
info = os.stat('datetime.py')
result = datetime.datetime.fromtimestamp(info.st_atime)
#os.system('notepad.exe')
os.path.join('D:\ ', 'deneme' , 'deneme1')
print(result)
print(name)


