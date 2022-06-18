#sonuc = open("newfile" , "w")
#print(sonuc)
#sonuc.close()

#file = open("D:/btkakademikurslar/python/1myapps/akif.docx" , "w")
#print(file)
#file.close() 

#file = open("D:/btkakademikurslar/python/1myapps/akif.txt" , "w" , encoding="utf-8")
#file.write("Merhaba ben Mehmet Akif türkçeKarakterler = ğıüşöç")
#file = open("D:/btkakademikurslar/python/1myapps/akif.txt" , "a" , encoding="utf-8")
#file.write("    Yanda verilen adım ve Türkçe karakterlerdir")
#file.close()

#file = open("D:/btkakademikurslar/python/1myapps/akif1.txt" , "x" , encoding="utf-8")


#file = open("D:/btkakademikurslar/python/1myapps/akif.txt" , "r" , encoding="utf-8")
#for i in file :
#    print(i)
#file.close()

#file = open("D:/btkakademikurslar/python/1myapps/akif.txt" , "r" , encoding="utf-8")
#read=file.read()
#print(read)


#content = file.readline()

#content = file.readlines()

#print(content[0])  
#file.close()

#with open("akif.txt","r",encoding="Utf-8") as file :
    #content = file.read()
    #print(content)
    #print(file.tell())
    #file.seek(10)
    #content = file.read()
    #print(content)

#with open("akif.txt","r+",encoding="Utf-8") as file :
    #print(file.read())

#with open("akif.txt","r+",encoding="Utf-8") as file :
    #file.seek(128)
    #file.write("deneme")
    
#with open("akif.txt","r+",encoding="Utf-8") as file :    
    #print(file.read())

#with open("akif.txt","r+",encoding="utf-8") as file :
    #content = file.read()
    #content = "Selamın Aleyküm\n" + content
    #file.seek(0)
    #file.write(content)

with open("akif.txt","r+",encoding="utf-8") as file :
    list = file.readlines()
    list.insert(1,"Zeynep\n")
    file.seek(0) 
    for i in list:
        file.write(i)
    print(list)


with open("akif.txt","r",encoding="utf-8") as file :
    print(file.read())