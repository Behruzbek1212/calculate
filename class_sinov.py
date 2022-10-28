class Odam:
    def __init__(self, ism,fam,yoshi):
        self.ism = ism
        self.fam = fam
        self.yoshi = yoshi

    def __str__(self):
        return f" {self.ism} {self.fam} {self.yoshi}"
    
odam = Odam("Begi", "Obloqulov","17")
print()


class Manzil(Odam):
    def __init__(self, ism,fam,yoshi,manzili,dom,uy):
        super().__init__(ism, fam, yoshi)
        self.manzili = manzili
        self.dom = dom
        self.uy = uy
    def m_chiqarish(self):
        print()
m = Manzil("Begi", "Obloqulov","17","Navoiy","118-a","407")
print(m.m_chiqarish())

class Kasbi(Odam):
    def __init__(self, ism,fam,yoshi,kasbi):
        super().__init__(ism, fam, yoshi)
        self.kasbi = kasbi

    def k_chiqarish(self):
        print()
kasb = Kasbi("Begi", "Obloqulov","17","Dasturchi")
print(kasb.k_chiqarish)
    