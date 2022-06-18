names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")
print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.

names.insert(0,"Sena")
print(names)

# 3-  "Deniz" ismini listeden siliniz.

#names.remove("Deniz")
#print(names)

# 4-  "Deniz" isminin indeksi nedir ?

res = names.index("Deniz")
print(res)

# 5-  "Ali" listenin bir elemanı mıdır ?

res1 = "Ali" in names
print(res1)

# 6-  Liste elemanlarını ters çevirin.

names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

string = "chevrolet , dacia "
res2 = string.split(",")
print(res2)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?

kc = min(years)
by = max(years)
print(kc,by)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

res3 = years.count(1998)
print(res3)

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

for i in range (3):
    marka = input("marka: ")
    markalar.append(marka)


print(markalar)