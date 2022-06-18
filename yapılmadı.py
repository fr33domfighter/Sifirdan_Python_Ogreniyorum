# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün
import datetime
tarih = input("Aracınızın trafiğe çıkış tarihini araya boşluk bırakarak (31 07 2020) giriniz: ")
tarih = tarih.split(" ")
simdi = datetime.datetime.now()
trafigecikis = datetime.datetime((int(tarih[0])),(int(tarih[1])),(int(tarih[2])))
fark = simdi - trafigecikis
days = fark.days
print(fark)
5