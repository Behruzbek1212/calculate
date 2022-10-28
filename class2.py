class Daryo: 
    def __init__(self,nomi,uzunligi,kengligi): 
        self.nomi = nomi
        self.uzunligi = uzunligi 
        self.kengligi = kengligi
    def __str__(self): 
        return f"nomi: {self.nomi} uzunligi: {self.uzunligi} kengligi: {self.kengligi}" 
 
d1 = Daryo("Amudaryo","10000","50") 
d2 = Daryo("Sirdaryo","5000", "40") 
d3 = Daryo("Nil","40000","30")
print(d1) 
print(d2) 
print(d3)