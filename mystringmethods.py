website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

res = "hello world".strip()
print (res)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

res1 = 'www.sadikturan.com'.strip("w.moc")
print(res1)

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

res2 =  course.lower()
print(res2)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

res3 = website.count("a")
print(res3)

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

res4 = website.startswith("www")
res4_1 = website.endswith("com")
print(res4,res4_1)

# 6-  'website' içinde '.com' ifadesi var mı?

res5 = website.find(".com")
print(res5)

# result = website.rindex('comm') # exception
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

res6 = course.isalpha()
print(res6)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

res7 = "contents".center(50,"*")
print(res7)

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

res8 = course.replace(" " , "-")
print(res8)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

res9 = "Hello World".replace("World" , "There")
print(res9)

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

res10 = course.split(" ")
res10 = course[2]
print(res10)

# result = result[2]   
