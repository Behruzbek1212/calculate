class Sayyoralar:
    def __init__(self,nomi,vazni):
        self.nomi = nomi
        self.vazni = vazni
    def chiq(self):
        print("Sayyora nomi: ",self.nomi,"Sayyora vazni: ",self.vazni)
s1 = Sayyoralar("Yer","4000000 kg")
s2 = Sayyoralar("Mars","5506500 kg")
s3 = Sayyoralar("Neptun","1331334 kg")
print(s1.chiq())
print(s2.chiq())
print(s3.chiq())

class Olchami(Sayyoralar):
    def __init__(self,nomi,vazni,olchami):
        super().__init__(nomi,vazni)
        self.olchami = olchami
    def chiq1(self):
        print("Sayyora nomi: ",self.nomi,"Sayyora vazni: ",self.vazni,"Sayyora o`lchami: ",self.olchami)
o1 = Olchami("Yer","4000000 kg","65641000 km kv")
o2 = Olchami("Mars","5506500 kg","100515100 km kv")
o3 = Olchami("Neptun","1331334 kg","4515410 km kv")
print(o1.chiq1())
print(o2.chiq1())
print(o3.chiq1())


class Tabiiy_yuldoshi(Sayyoralar):
    def __init__(self,  nomi, vazni,yuldoshi):
        super().__init__(nomi,vazni)
        self.yuldoshi = yuldoshi
    def chiq2(self):
        print("Sayyora nomi: ",self.nomi,"Sayyora vazni: ",self.vazni,"Sayyora yo`ldoshi: ",self.yuldoshi)
y1 = Tabiiy_yuldoshi("Yer","4000000 kg","Oy")
y2 = Tabiiy_yuldoshi("Mars","5506500 kg","Quyosh, Oy")
y3 = Tabiiy_yuldoshi("Neptun","1331334 kg","Tabiiy yo`ldoshi yo`q")
print(y1.chiq2())
print(y2.chiq2())
print(y3.chiq2())