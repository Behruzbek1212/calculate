s = int(input("Hayvonlar ro`yxati kerak bolsa 2ni bosing, odamlar royxati kerak bolsa 1 ni bosing: ")) 
 
if s == 1: 
    class Odam: 
        def __init__(self,ism,fam,yosh): 
            self.ism = ism 
            self.fam = fam 
            self.yosh = yosh 
        def __str__(self): 
            return f"ismi: {self.ism},familiya: {self.fam},ishi: {self.yosh}" 
 
    o1 = Odam("Diyor","yuldashev","16") 
    o2 = Odam("Shavkat","imomov", "17") 
    print(o1) 
    print(o2) 
elif s == 2: 
        class Hayvon: 
            def __init__(self,turi,laqabi,rangi): 
                self.turi = turi 
                self.laqabi = laqabi 
                self.rangi = rangi 
            def __str__(self): 
                return f"turi: {self.inomi},laqabi: {self.laqabi},rangi: {self.rangi}" 
 
        h1 = Hayvon("It","tommy","oq") 
        h2 = Hayvon("Mushuk","jery","qora") 
        print(h1) 
        print(h2) 
else: 
    print()