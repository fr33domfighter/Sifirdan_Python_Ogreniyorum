#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
a = int(input("Bir sayı giriniz: "))
if 0 < a and a%2==0 :
    print(f"Girdiğiniz sayı {a} pozitif ve çifttir.")
elif a < 0 :
    print(f"Girdiğiniz sayı {a} negatiftir.")
elif a%2!=0 :
    print(f"Girdiğiniz sayı {a} tektir.")