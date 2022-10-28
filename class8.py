class Mashina: 
    def __init__(self,nomi,otkuchi,tezlik): 
        self.nomi = nomi 
        self.otkuchi = otkuchi 
        self.tezlik = tezlik 
    def __str__(self): 
        return f"nomi: {self.nomi} otkuchi: {self.otkuchi} tezlik: {self.tezlik}" 
 
m1 = Mashina("BMW","1120","360") 
m2 = Mashina("Mers","1000", "340") 
m3 = Mashina("Bugatti","1200","420")
print(m1) 
print(m2) 
print(m3)