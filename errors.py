# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
for i in liste:
    try:
        i = int(i)
    except ValueError:
        continue
    print(i)

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    giris = input("Bir sayı giriniz: ")
    if giris == "q":
        break
    try:
        giris = int(giris)
        print(f"Girdiğiniz sayı : {giris}")
    except ValueError:
        print("Lütfen sayı giriniz: ")
        continue


# 3: Girilen parola içinde türkçe karakter hatası veriniz.

def checkPwd(pwd):
    for t in pwd:
        if t in turkceKarakterler:
            raise TypeError("Yazdığınız parolada Türkçe karakter bulunuyor , bulunamaz.")


turkceKarakterler = "ğıüşöçİ"
pwd = input("Parolanızı girin: ")
while True:
    if pwd in turkceKarakterler:
        try:
            checkPwd(pwd)
        except TypeError as hata:
            print(hata)
        pwd = input("Parolanızı girin: ")
    else:
        print("Girmiş olduğunuz parola kurallara uygun.")
        break


# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1

    for i in range(1, x + 1):
        result *= i

    return result


for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
