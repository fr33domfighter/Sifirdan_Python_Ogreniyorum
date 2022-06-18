print("""merhaba ben bilgisayar 
1-100 arasında aklımdan bir sayı tuttum 
sende tuttuğum sayıyı bilmeye çalış 
bakalım kaç seferde bulabileceksin.""")
import random
randomNumber = random.randint(1,100)
hak = 100 
sayac = 0
while 0 < hak :
    sayac += 1
    tahmin = int(input("sayı tahmininizi giriniz: ")) 
    puan = 100 - (sayac*5)    
    if tahmin == randomNumber :
        print(f"""Tebrikler oyunu tamamladınız.
        {sayac} denemede bildiniz.
        {puan} aldınız.""")
        break
    elif tahmin < randomNumber :
        print("daha yüksek bir sayı girin.")
    else :
        print("daha küçük bir sayı girin.")
    