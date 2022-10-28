class Tog: 
    def __init__(self,joyi,nomi,balandligi): 
        self.joyi = joyi 
        self.nomi = nomi 
        self.balandligi = balandligi 
    def __str__(self): 
        return f"joyi: {self.joyi} nomi: {self.nomi} balandligi: {self.balandligi}" 
 
t1 = Tog("veytnam","everesrt","8850") 
t2 = Tog("uzbekistan","tyanshan", "3642") 
t3 = Tog("london","nevis","5319")
print(t1) 
print(t2) 
print(t3)