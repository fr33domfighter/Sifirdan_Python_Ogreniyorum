'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''
sayi = int(input("bir sayı giriniz: "))
if sayi == 1 :
    print("girdiğiniz sayı asal değildir.")
elif sayi % sayi == 0 :
    print("girdiğiniz sayı asaldır.")
else :
    print("girdiğiniz sayı asal değildir.")