#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#tek sayıları ekrana yazdırın.
baslangic = int(input("Başlangıç sayısını giriniz: "))
bitis = int(input("Bitiş sayısını giriniz: "))
i= baslangic
while i<bitis :
    i += 1
    if i % 2 != 0 :
        print(i)
