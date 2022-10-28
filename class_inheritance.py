class Odam:
    def __init__(self, ism,fam,yoshi):
        self.ism = ism
        self.fam = fam
        self.yoshi = yoshi

    def __str__(self):
        return f" {self.ism} {self.fam} {self.yoshi}"
    
odam = Odam("Begi", "Obloqulov","17")
print(odam)


class Manzil(Odam):
    def __init__(self, ism,fam,yoshi,manzili,dom,uy):
        super().__init__(ism, fam, yoshi)
        self.manzili = manzili
        self.dom = dom
        self.uy = uy
    def m_chiqarish(self):
        print()
m = Manzil("Navoiy","118-a","407",3, 1, 2)
print(m)

class Kasbi(Odam):
    def __init__(self, ism,fam,yoshi,manzili,kasbi):
        super().__init__(ism, fam, yoshi)
        self.manzili = manzili
        self.kasbi = kasbi

    def k_chiqarish(self):
        print()
kasb = Kasbi("Navoiy","Dasturchi",4,45,4)
print(kasb)
    