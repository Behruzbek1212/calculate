class Xona: 
    def __init__(self,boyi,eni,balandligi): 
        self.boyi = boyi 
        self.eni = eni 
        self.balandligi = balandligi 
    def __str__(self): 
        return f"boyi: {self.boyi} eni: {self.eni} balandligi: {self.balandligi}" 
 
x1 = Xona("50","20","3") 
x2 = Xona("40","15", "2.5") 
x3 = Xona("32","12","4")
print(x1) 
print(x2) 
print(x3)