
import turtle #turtle isimli modülü pythona yükler
pencere=turtle.Screen()#kaplumbağalar için bir pencere açıp bunu pencere değişkenine ata
pencere.bgcolor("purple")
pencere.title("merhaba ad")
t=turtle.Turtle() #t isimli bir kaplumbağa oluşturduk
t.shape("square")
t.color("white")
#t.penup() #kalemi kaldır
size=20
for i in range(20):
    t.stamp()
    size=size+3
    t.forward(size)
    t.right(30)
t.circle(50)

renkler=["yellow","red","black","blue","gray"]
for i in renkler:
    t.color(i)
    t.forward(200) #t yi 50 birim ilerlet
    t.left(144) #t yi 90 derece döndür
pencere.mainloop
