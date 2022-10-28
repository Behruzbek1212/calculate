class Hayvon: 
    def __init__(self,turi,laqabi,rangi): 
        self.turi = turi 
        self.laqabi = laqabi 
        self.rangi = rangi 
    def __str__(self): 
        return f"turi: {self.turi}, laqabi: {self.laqabi}, rangi: {self.rangi}" 
 
a = Hayvon("It","Leo","oq") 
a2 = Hayvon("Mushuk","Nastya","oq") 
a3 = Hayvon("Ot","Qorabayr","qora")
print(a) 
print(a2)
print(a3)