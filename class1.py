class Odam: 
    def __init__(self,ism,fam,yosh): 
        self.ism = ism 
        self.fam = fam 
        self.yosh = yosh 
    def __str__(self): 
        return f"ismi: {self.ism},familiya: {self.fam},ishi: {self.yosh}" 
 
o1 = Odam("Diyor","yuldashev","16") 
o2 = Odam("Shavkat","imomov", "17") 
o3 = Odam("Doni","doniyorov","15")
print(o1) 
print(o2) 
print(o3)