

def aslsayı(sayı1,sayı2):
    liste = []
    for sayı in range(sayı1,sayı2+1):
        if sayı>1 :
            for i in range (2,sayı):
                if sayı%i==0:
                    break
            else:
                liste.append(sayı)
            print(liste)
                

sayı1= int(input("sayı1:"))
sayı2 = int(input("sayı2:"))

print(aslsayı(sayı1,sayı2))





