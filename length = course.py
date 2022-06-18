website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

lencourse = (len(course))
print(lencourse)

www = website[7:10]
print(www)

lenweb = len(website)
print(website[lenweb-3:lenweb])

ilk = course[:15]
print(ilk)
son = (course[lencourse-15:lencourse])
print(son)

ters = course[::-1]
print(ters)

name = "Mehmet Akif "
surname = "Arslan" 
age = 15
job = "mühendis"
print(f"Benim adım", {name} , "soyadım" , {surname} ,"yaşım" , {age} ,"ve" , "mesleğim" , {job})

h = "hello" 
w = "world"
w = w.capitalize()
print(h,w)

a = "abc" *3
print(a)





