class Davlat: 
    def __init__(self,davlat,poytaxt,joy): 
        self.davlat = davlat 
        self.poytaxt = poytaxt 
        self.joy = joy 
    def __str__(self): 
        return f"davlat: {self.davlat} poytaxt: {self.poytaxt} joyi: {self.joy}" 
 
d1 = Davlat("Uzbekistan","Toshkent","yunusobod") 
d2 = Davlat("AQSH","Washintong", "newstreet") 
d3 = Davlat("Russia","Moskva","bilmadim")
print(d1) 
print(d2) 
print(d3)