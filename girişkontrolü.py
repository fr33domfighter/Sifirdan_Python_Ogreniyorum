#3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

email = 'email@sadikturan.com'
password = 'abc123'
girilenmail = input("Mail adresinizi giriniz: ")
girilenparola = input("Parolanızı giriniz: ")
if email == girilenmail :
    if password == girilenparola:
        print(f"Mail adresiniz {girilenmail} ve parolanız {girilenparola} doğru giriş başarılı. ")
    else:
        print("Parolanız yanlış.")
else:
    print("Mailinizi yanlış girdiniz.")        