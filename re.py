import re
str = "selam ben mehmet"
#res = re.findall("ben" , str)
#res = re.split(" ", str)
#res = re.sub(" " ,"-",str)
res = re.search("selam",str).span()
print(res)

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

   
"""
# .. iki nokta 4 basamaklı bir str de aranırsa 
# 2 çıktı döner
## ... bütün üçlü gruplar alınır
### sel.m yine selam ifadesi döner
result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result = re.findall("^P",str)


"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
# m den hemen sonra a var mı ve a dan hemen sonra 
# n var mı ona bakar eğer a dan hemen önce m ve 
# hemen sonra n yoksa dönüş olmaz yani a nın olup
# olmaması ile ilgilenir ve hiç olmasa da dönüş olur
# çünkü 0 ı da sayar

result = re.findall("sa*t",str)

"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
# burada ise 0 sayılmaz aranan karakter hiç yoksa
# dönüş olmaz en az bir tane olmalıdır
result = re.findall("sa+t",str)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma?n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa?t",str)

"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    dönüş olmaz
            ade =>    1 dönüş olur
            acdbea => 3 dönüş olur
"""

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""



"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => 'the' string in başındamı

        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)

    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => 'the' string in sonunda mı

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => 'the' kelimenin in başında mı? her kelime için arama yapar
         the\b => 'the' kelimenin in sonunda mı? her kelime için arama yapar

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => 'the' kelimenin in başında değil mi? her kelime için arama yapar
         the\B => 'the' kelimenin in sonunda değil mi? her kelime için arama yapar
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""
# fazlası için 
# https://www.w3schools.com/python/python_regex.asp

print(result)