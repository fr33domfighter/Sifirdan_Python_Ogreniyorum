#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
        #Formül: (Kilo / boy uzunluğunun karesi)
        #Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
        #0-18.4    => Zayıf 
        #18.5-24.9 => Normal  
        #25.0-29.9 => Fazla Kilolu
        #30.0-34.9 => Şişman (Obez)
ad = input("Adınızı giriniz: ")
isim = ad.title()
kilo = float(input("Kilonuzu giriniz: "))
boy = float(input("Metre cinsinden (ör:1.70) boyunuzu giriniz: "))
formul = (kilo)/(boy**2) or (kilo)/((boy/10)**2) 
if formul >= 0 and formul <= 18.4 :
   print(f"Merhaba {isim} kütle endeksiniz {formul}'dur.Zayıfsınız. ")
elif formul >= 18.5 and formul <= 24.9:
     print(f"Merhaba {isim} kütle endeksiniz {formul}'dur.Normal kilodasınız. ")
elif formul >= 25.0 and formul <= 29.9:
     print(f"Merhaba {isim} kütle endeksiniz {formul}'dur.Fazla kilolusunuz. ")
elif formul >= 30.0 and formul <= 34.9:
     print(f"Merhaba {isim} kütle endeksiniz {formul}'dur.Maalesef obezsiniz. ")
else:
     print(f"Sevgili {isim} isimli kullanıcı hatalı bilgi girişi yaptınız.")