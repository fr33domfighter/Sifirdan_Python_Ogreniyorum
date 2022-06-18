# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#yazdırın.
numbers = []
i=0
while i < 5 :
    sayi = int(input("Bir sayı giriniz: "))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)


