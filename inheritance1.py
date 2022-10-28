class Daryo:
    def __init__(self,nomi,uzunligi):
        self.nomi = nomi
        self.uzunligi = uzunligi
    def chiqarish1(self):
       print("nomi: ",self.nomi, "uzunligi: ",self.uzunligi)
daryo1 = Daryo("Nil,","10000,")
daryo2 = Daryo("Amudaryo","5000")
daryo3 = Daryo("Sirdaryo","4000")
print(daryo1.chiqarish1())
print(daryo2.chiqarish1())
print(daryo3.chiqarish1())


class Eni(Daryo):
    def __init__(self,nomi,uzunligi,eni):
        super().__init__(nomi,uzunligi)
        self.eni = eni
    def chiqarish2(self):
        print("nomi: ",self.nomi,"uzunligi: ",self.uzunligi,"eni: ",self.eni)
e1 = Eni("Nil,","10000,","100")        
e2 = Eni("Amudaryo","5000","20")
e3 = Eni("Sirdaryo","4000","30")
print(e1.chiqarish2())
print(e2.chiqarish2())
print(e3.chiqarish2())


class Joyi(Daryo):
    def __init__(self,nomi,uzunligi,joyi):
        super().__init__(nomi,uzunligi)
        self.joyi = joyi
    def chiqarish3(self):
        print("nomi: ",self.nomi,"uzunligi: ",self.uzunligi,"joyi: ",self.joyi)
d1 = Joyi("Nil,","10000,","Misir")
d2 = Joyi("Amudaryo","5000","Uzbekistan")
d3 = Joyi("Sirdaryo","4000","Uzbekistan")
print(d1.chiqarish3())
print(d2.chiqarish3())
print(d3.chiqarish3())