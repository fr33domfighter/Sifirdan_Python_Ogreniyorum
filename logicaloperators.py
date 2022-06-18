
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayı = int(input("bir sayı giriniz: "))
res = sayı<100 and sayı>0
print(res)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayı = int(input("bir sayı giriniz: "))
res = sayı>0 and sayı%2 == 0
print(res)
 
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

email = 'email@sadikturan.com'
password = 'abc123'
gırılenMaıl = input("emailinizi giriniz: ")
gırılenSifre = input("şifrenizi giriniz: ")
res = gırılenMaıl == email and gırılenSifre == password
print(res)

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input("a: "))
b = int(input("b "))
c = int(input("c: "))
res = a>b and a>c 
print(f"girdiğiniz sayılar büyükten küçüğe sıralandığında a en büyük sayıdır {res}")
res1 = b>a and b>c 
print(f"girdiğiniz sayılar büyükten küçüğe sıralandığında b en büyük sayıdır {res1}")
res2 = c>a and c>b
print(f"girdiğiniz sayılar büyükten küçüğe sıralandığında c en büyük sayıdır {res2}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("1.vize notunuzu giriniz: "))
vize2 = float(input("2.vize notunuzu giriniz: "))
final = float(input("final notunuzu giriniz: "))
ort = (((vize1+vize2)/2)*0.6) + (final*0.4)
res = ort >= 50 and final>=50
res = final == 70 or ort >= 50
print(f"ortalamanız: {ort} sınıfı geçip geçmeme durumunuz {res}")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input("adınızı giriniz: ")
kilo = float(input("kilonuzu giriniz: "))
boy = float(input("boyunuzu giriniz: "))
formul = (kilo)/(boy**2)
Zayıf = formul >= 0 and formul <= 18.4
Normal = formul >= 18.5 and formul <= 24.9
fk = formul >= 25.0 and formul <= 29.9
obez = formul >= 30.0 and formul <= 34.9
print(f"{ad} kilo endeksiniz {formul} ve kilo dğerlendirme durumunuz zayıf {Zayıf}")
print(f"{ad} kilo endeksiniz {formul} ve kilo dğerlendirme durumunuz normal {Normal}")
print(f"{ad} kilo endeksiniz {formul} ve kilo dğerlendirme durumunuz fazla kilolu {fk}")
print(f"{ad} kilo endeksiniz {formul} ve kilo dğerlendirme durumunuz obez {obez}")
