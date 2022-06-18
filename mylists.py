# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ["bmw" , "mercedes" , "opel" , "mazda"]

# 2-  Liste Kaç elemanlıdır ?

print(len(arabalar))

# 3-  Listenin ilk ve son elemanı nedir ?

ilk = arabalar[0]
son = arabalar[-1]
print("listenen ilk elemanı", ilk , "dir." )
print("listenen son elemanı", son , "dır." )

# 4-  Mazda değerini Toyota ile değiştirin.
# arabalar[-1]= 'Toyota'

res = arabalar[-1] = "toyota"
print(arabalar)

# 5-  Mercedes listenin bir elemanı mıdır ?

res1 = "mercedes" in arabalar
print(res1)


# 6-  Listenin -2 indeksindeki değer nedir ?

res2 = arabalar[-2]
print(res2)

# 7-  Listenin ilk 3 elemanını alın.

res3 = arabalar[0:3]
print(res3)

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

arabalar[-2:] = ["toyota" , "renault"]
print(arabalar)


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

res5 = arabalar.append("audi")
res5_1 = arabalar.append("nissan")
print(arabalar)

# 10- Listenin son elemanını silin.

del arabalar[-1]
print(arabalar)

# 11- Liste elemanlarını tersten yazdırınız.

res7 = arabalar[::-1]
print(arabalar)

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ["Yiğit" , "Bilgi" , 2010 ,[70,60,70]]
studentB = ["Sena Turan" , 1999 , [80,80,70]]
studentC = ["Ahmet Turan" , 1998 , [80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

print(f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}")


