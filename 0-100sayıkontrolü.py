#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a = int(input("bir sayı giriniz: "))
if 0 <= a <= 100 :
    print(f"Girdiğiniz sayı {a} 0 ile 100 arasındadır.")
else : 
    print(f"Girdiğiniz sayı {a} 0 ile 100 arasında değildir.")