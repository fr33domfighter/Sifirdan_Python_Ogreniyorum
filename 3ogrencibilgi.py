# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
ogrenciler = {}
for i in range (3) :
    number = input("öğrenci numarasını giriniz: ")
    name = input("öğrenci adını giriniz: ")
    surname = input("öğrenci soyadını giriniz: ")
    phone = input("öğrenci telefon numarasını giriniz: ")
    ogrenciler.update({
        number : {
            "ad":name,
            "soyad":surname,
            "telefon":phone 
        }
    })
    print("*"*50)
ogrno = input("bilgilerini istediğiniz öğrencinin numarasını girin: ")
ogrenci = ogrenciler[ogrno]
print(f"""
aradığınız {ogrno} nolu 
öğrencinin adı: {ogrenci['ad']} 
soyadı:{ogrenci['soyad']}  
telefonu {ogrenci['telefon']} """
)