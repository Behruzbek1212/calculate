class Uylar:
    def __init__(self,boyi,eni):
        self.boyi = boyi
        self.eni = eni
    def chiq(self):
        print("Uyning bo`yi: ",self.boyi,"Uyning eni: ",self.eni)
u1 = Uylar("5 mert","8 metr")
u2 = Uylar("4 metr","6 metr")
u3 = Uylar("3 metr","5 metr")
u1.chiq()
u2.chiq()
u3.chiq()


class Kvadrati(Uylar):
    def __init__(self, boyi, eni,kv):
        super().__init__(boyi, eni)
        self.kv = kv
    def chiq1(self):
        print("Uyning bo`yi: ",self.boyi,"Uyning eni: ",self.eni,"Uyning kvadrati: ",self.kv)
k1 = Kvadrati("5 mert","8 metr","40 kv metr")
k2 = Kvadrati("4 metr","6 metr","24 kv metr")
k3 = Kvadrati("3 metr","5 metr","15 kv metr")
print(k1.chiq1())
print(k2.chiq1())
print(k3.chiq1())

class Narxi(Uylar):
    def __init__(self, boyi, eni,narxi):
        super().__init__(boyi,eni)
        self.narxi = narxi
    def chiq2(self):
        print("Uyning bo`yi: ",self.boyi,"Uyning eni: ",self.eni,"Uyning narxi: ",self.narxi)
n1 = Narxi("5 mert","8 metr","100 million so`m")
n2 = Narxi("4 metr","6 metr","80 million so`m")
n3 = Narxi("3 metr","5 metr","55 million so`m")
print(n1.chiq2())
print(n2.chiq2())
print(n3.chiq2())