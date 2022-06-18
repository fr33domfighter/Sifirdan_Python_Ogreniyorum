#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input("Bir sayı giriniz: "))
b = int(input("Bir sayı giriniz: "))
c = int(input("Bir sayı giriniz: "))
if a > b and a > c :
    print("Girdiğiniz sayılar arasından 1. sayı en büyüktür. ")
elif b > a and b > c :
    print("Girdiğiniz sayılar arasından 2. sayı en büyüktür.")
elif c > a and c > b :
    print("Girdiğiniz sayılar arasından 3. sayı en büyüktür.")
