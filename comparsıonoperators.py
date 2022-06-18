
# 1- Girilen 2 sayıdan hangisi büyüktür ?

#a = int(input("1. sayıyı giriniz :" ))
#b = int(input("2. sayıyı giriniz :"))
#if a<b :
 #   print("2. sayı büyüktür.")
#else :
 #   print("1. sayı büyüktür")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

#vize1 = float(input("1. vizeyi giriniz :"))
#vize2 = float(input("2. vizeyi giriniz :"))
#final = float (input("finali giriniz :"))
#ort =  (((vize1+vize2)/2)*0.6) + (final *0.4)
#print(ort)
#if ort < 50 :
 #   print("kaldınız")
#else :
 #   print("geçtiniz")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

#a = int(input("bir sayı giriniz :"))
#if a%2 == 0 :
 #   print("girdiğiniz sayı çifttir.")
#else :
 #   print("girdiğiniz sayı tektir.")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

#a = int(input("bir sayı girin :"))
#if a < 0 :
 #   print("girdiğiniz sayı negatiftir.")
#else :
 #   print("girdiğiniz sayı pozitiftir.")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = 'email@sadikturan.com'
password = 'abc123'

mail = input("emailinizi girin :")
pas = input("şifrenizi girin :")
check = mail == email
check1 = pas == password
print(f"mailiniz doğru mu? {check} şifreniz doğru mu? {check1}")