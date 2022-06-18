# 5- Ürünlerin fiyatları toplamı nedir ?
urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]
for i in urunler:
    print(i)
top = 0
for urun in urunler:
    fiyat = int(urun["price"])
    top += fiyat
print(top)