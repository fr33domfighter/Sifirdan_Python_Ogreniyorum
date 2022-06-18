# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

def birKez(metin,adet):
    print(metin*adet)
birKez("merhaba\n",3)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

def sinirsiz(*parametreler):
    list = []
    for ceviri in parametreler :
        list.append(ceviri)
    return list
print(sinirsiz(2,3,4,5,6,768,68,76,68,67,68))

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalSayi(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi%i == 0:
                    break
            else:
                print(sayi)
sayi1 = int(input('1. sayıyı giriniz: '))
sayi2 = int(input('2. sayıyı giriniz: '))
asalSayi(sayi1,sayi2)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def tamBölenleriBul(sayi):
    tamBolenler = []
    for i in range (2,sayi):
        if sayi%i == 0:
            tamBolenler.append(i)
    return tamBolenler
print(tamBölenleriBul(20))