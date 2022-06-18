def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2]) 

    ortalama = (not1+not2+not3)/3

    if 90<=ortalama<=100:
        harf = "AA"
    elif 85<=ortalama<=89:
        harf = "BA"
    elif 80<=ortalama<=84:
        harf = "BB"
    elif 75<=ortalama<=79:
        harf = "CB"
    elif 70<=ortalama<=74:
        harf = "CC"
    elif 65<ortalama<=69:
        harf = "DC"
    elif 60<=ortalama<=64:
        harf = "DD"
    elif 50<=ortalama<=59:
        harf = "FD"
    elif 0<=ortalama<49:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"


def ortalamalariOku():
    with open("sinavNotları.txt" , "r" , encoding="utf8") as file:
        for satir in file:
            print(notHesapla(satir))


def notGir():
    ad = input("Öğrenci adı:")
    soyad = input("Öğrenci soyadı:")
    not1 = input("Not1:")
    not2 = input("Not2:")
    not3 = input("Not3:")

    with open("sinavNotları.txt" , "a" , encoding="utf8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3+"\n")


def notlarıKayıtEt():
    with open("sinavNotları.txt" , "r" , encoding="utf8") as file:
        liste = []

        for i in file:
            liste.append(notHesapla(i))

        with open("sonuclar.txt" , "w" , encoding="utf8") as file2:
            for i in liste:
                file2.write(i)


while True:
    print("""Lütfen notları girdikten sonra kaydetmeyi unutmayın!!!""")
    islem= input("1-Notları oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n")
    if islem == "1":
        ortalamalariOku()
    elif islem=="2":
        notGir()
    elif islem=="3":
        notlarıKayıtEt()
    else:
        break
