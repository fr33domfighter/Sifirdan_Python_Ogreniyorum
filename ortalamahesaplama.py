ad = input("İsminizi giriniz: ")
ısım = ad.upper()
yazili1 = float(input("1. yazılı notunuzu giriniz: "))
yazili2 = float(input("2. yazılı notunuzu giriniz: "))
sozlu = float(input("1. Sözlü notunuzu giriniz: "))
sozlu1 = float(input("2. Sözlü notunuzu giriniz: "))
sozlu2 =float(input("3. Sözlü notunuzu giriniz: "))
ort = ((yazili1+yazili2+sozlu+sozlu1+sozlu2)/5)
if 0 <= ort and 24 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 0 aldınız. ") 
elif 25 <= ort and 44 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 1 aldınız. ")
elif 45 <= ort and 54 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 2 aldınız. ")
elif 55 <= ort and 69 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 3 aldınız. ")
elif 70 <= ort and 84 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 4 aldınız. ")
elif 85 <= ort and 100 >= ort :
    print(f"Sevgili öğrencimiz {ısım} not ortalamanız {ort} ve not ortalamanıza göre 5'lik punlamaya göre 5 aldınız. ")
else:
    print('Yanlış bilgi girdiniz.')
