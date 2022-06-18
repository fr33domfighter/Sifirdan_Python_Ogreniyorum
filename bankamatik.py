# Bankamatik Uygulaması

#para yatırma fonksiyonu ekle bir ek hesap limiti olup önce o limitin tamamlanması gerekir

#bir işlem menüsü yap
print("""İŞLEM MENÜSÜ
1-BAKİYE SORGULAMA
2-PARA YATIRMA
3-PARA ÇEKME
YAPPMAK İSTEDİĞİNİZ İŞLEME GÖRE İLGİLİ NUMARAYA BASINIZ.""")

işlem = int(input("Yapmak istediğiniz işlem numarasını giriniz: "))

SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

elif işlem == 2 :
    def paraYatırma(hesap,miktar):
        print(f"Merhaba {hesap['ad']}")
        yatiralacakMiktar = int(input("yatırmak istediğiniz para miktarını giriniz: "))
        hesap += yatiralacakMiktar
        print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")



def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)

paraCek(SadikHesap, 3000)

print('*****************')

paraCek(SadikHesap, 2000)