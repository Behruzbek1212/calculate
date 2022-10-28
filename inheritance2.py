class Telefon:
    def __init__(self,nomi,xotirasi):
        self.nomi = nomi
        self.xotirasi = xotirasi
    def chiq1(self):
        print("Telefon nomi: ",self.nomi,"Xotirasi: ",self.xotirasi)
t1 = Telefon("Iphone 14 pro max","256 gb")
t2 = Telefon("Redmi 11 pro","128 gb")
t3 = Telefon("Honor x9","512")
print(t1.chiq1())
print(t2.chiq1())
print(t3.chiq1())


class Dizayni(Telefon):
    def __init__(self,nomi,xotirasi,rangi):
        super().__init__(nomi,xotirasi)
        self.rangi = rangi
    def chiq2(self):
        print("Telefon nomi: ",self.nomi,"Xotirasi: ",self.xotirasi,"Rangi: ",self.rangi)
d1 = Dizayni("Iphone 14 pro max","256 gb","Qora")
d2 = Dizayni("Redmi 11 pro","128 gb","Oq")
d3 = Dizayni("Honor x9","512","Moviy")
print(d1.chiq2())
print(d2.chiq2())
print(d3.chiq2())


class Kamera(Telefon):
    def __init__(self,nomi,xotirasi,pixel):
        super().__init__(nomi,xotirasi)
        self.pixel = pixel
    def chiq2(self):
        print("Telefon nomi: ",self.nomi,"Xotirasi: ",self.xotirasi,"Kamera pikseli: ",self.pixel)
k1 = Kamera("Iphone 14 pro max","256 gb","36 pixel")
k2 = Kamera("Redmi 11 pro","128 gb","108 pixxel")
k3 = Kamera("Honor x9","512","64 pixel")
print(k1.chiq2())
print(k2.chiq2())
print(k3.chiq2())