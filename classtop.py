from traceback import print_tb


class Odam:
    def __init__(self, ism,fam,yosh):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh
    def __str__(self):
        return f"ism: {self.ism} fam: {self.fam} yosh: {self.yosh}"
o1 = Odam("Behruzbek","Obloqulov","17")
o2 = Odam("Shokirjon","Shokirov","18")
print(o1)
print(o2)
        















        