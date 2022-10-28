class Odam:
    def init(self, ism,fam,yoshi):
        self.ism = ism
        self.fam = fam
        self.yoshi = yoshi

    def str(self):
        return f" {self.ism} {self.fam} {self.yoshi}"
    
odam = Odam("Begi", "Obloqulov","17")
print(odam)


class Manzil(Odam):
    def init(self, ism,fam,yoshi,manzili,dom,uy):
        super().init(ism, fam, yoshi)
        self.manzili = manzili
        self.dom = dom
        self.uy = uy
    def m_chiqarish(self):
        print()
m = Manzil("Navoiy","118-a","407",3, 1, 2)
print(m)

class Kasbi(Odam):
    def init(self, ism,fam,yoshi,manzili,kasbi):
        super().init(ism, fam, yoshi)
        self.manzili = manzili
        self.kasbi = kasbi

    def k_chiqarish(self):
        print()
kasb = Kasbi("Begi","Obloqulov","17","Navoiy","Dasturchi")
print(kasb)