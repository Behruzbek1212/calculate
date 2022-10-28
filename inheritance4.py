class Dustlarim:
    def __init__(self,ismi,fam):
        self.ismi = ismi
        self.fam = fam
    def chiq(self):
        print("Ismi: ",self.ismi,"Familiyasi: ",self.fam)
d1 = Dustlarim("Shokirjon","Shokirov")
d2 = Dustlarim("Muhammadjon","Doniyorov")
d3 = Dustlarim("Otabek","Asatov")
print(d1.chiq())
print(d2.chiq())
print(d3.chiq())

class Shahri(Dustlarim):
    def __init__(self, ismi, fam,shahri):
        super().__init__(ismi, fam)
        self.shahri = shahri
    def chiq1(self):
        print("Ismi: ",self.ismi,"Familiyasi: ",self.fam,"Yashash joyi: ",self.shahri)
sh1 = Shahri("Shokirjon","Shokirov","Buxoro")
sh2 = Shahri("Muhammadjon","Doniyorov","Navoiy")
sh3 = Shahri("Otabek","Asatov","Navoiy")
print(sh1.chiq1())
print(sh2.chiq1())
print(sh3.chiq1())

class Qiziqishi(Dustlarim):
    def __init__(self, ismi, fam,qiziqish):
        super().__init__(ismi, fam)
        self.qiziqish = qiziqish
    def chiq2(self):
        print("Ismi: ",self.ismi,"Familiyasi: ",self.fam,"Qiziqadigan sohasi: ",self.qiziqish)
q1 = Qiziqishi("Shokirjon","Shokirov","GID")
q2 = Qiziqishi("Muhammadjon","Doniyorov","Dasturchi")
q3 = Qiziqishi("Otabek","Asatov","Biznes")
print(q1.chiq2())
print(q2.chiq2())
print(q3.chiq2())