class Komp: 
    def __init__(self,nomi,ozu,xotira): 
        self.nomi = nomi 
        self.ozu = ozu 
        self.xotira = xotira 
    def __str__(self): 
        return f"nomi: {self.nomi} ozu: {self.ozu} xotira: {self.xotira}" 
 
k1 = Komp("Lenovo","4","556") 
k2 = Komp("Acer","8", "1000") 
k3 = Komp("hp","2","556")
print(k1) 
print(k2) 
print(k3)   