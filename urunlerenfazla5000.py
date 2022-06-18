# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]
for fiyat in urunler:
    if int(fiyat["price"]) <= 5000:
        print(fiyat["name"])
