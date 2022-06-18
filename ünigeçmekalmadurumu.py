#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
        #Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
        #a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
        #b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input("1.vize notunuzu giriniz: "))
vize2 = float(input("2.vize notunuzu giriniz: "))
final = float(input("final notunuzu giriniz: "))
ort = (((vize1+vize2)/2)*0.6) + (final*0.4)
if (ort >=50):
    print(f'öğrencinin ortalaması: {ort} ve geçme durumu: başarılı')
else:
    if (final>=70):
        print(f'öğrencinin ortalaması: {ort} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'öğrencinin ortalaması: {ort} ve geçme durumu: başarısız')