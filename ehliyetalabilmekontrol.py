ısım = input("İsminizi giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
egıtım = input("Eğitim durumunuzu giriniz: ")
ad = ısım.title()
eg = egıtım.capitalize()
if yas >= 18 :
    print("Ehliyet almak için yaşınız tutuyor.")
else :
    print("Ehliyet alamk için yaşınız tutmuyor.")
if eg == "Lise" or eg == "Üniversite" :
    print("Ehliyet almak için eğitim durumunuz müsait.")
else :
    print("Ehliyet almak için eğitim durumunuz müsait değil.")
if yas >= 18 and egıtım == "Lise" or eg == "Üniversite" :
    print(f"Merhaba {ad} yaşınız ve eğitim durumunuz müsait ehliyet alabilirsiniz.")
else :
    print((f"Merhaba {ad} yaşınız tutmadığından veya eğitim durumunuz müsait olmadığından ehliyet alamazsınız."))