class Gul: 
    def __init__(self,nomi,turi,rangi): 
        self.nomi = nomi 
        self.turi = turi 
        self.rangi = rangi 
    def __str__(self): 
        return f"nomi: {self.nomi} turi: {self.turi} rangi: {self.rangi}" 
 
g1 = Gul("lola","gulsimon","qizil") 
g2 = Gul("atirgul","butasimon", "qizil") 
g3 = Gul("kaktus","daraxtsimon","yashil")
print(g1) 
print(g2) 
print(g3)