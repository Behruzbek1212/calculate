class  Kitoblar:
    def __init__(self, nomi,hikoyasi,xulosa):
        self.nomi = nomi
        self.hikoyasi = hikoyasi
        self.xulosa = xulosa
    def __str__(self):
    #    return f"Nomi: {self.nomi} Hikoyasi {self.hikoyasi} xulosa {self.xulosa}"
        return "nomi: {}, hikoyasi: {}, xulosa :{}".format(self.nomi,self.hikoyasi,self.xulosa)
k1 = Kitoblar("shum bola", "bir balo", "rostgoylik")
k2 = Kitoblar("fewf","gegfg","grtrgg")
k3 = Kitoblar("feregg3r","wefefe","erg3g")
print(k1)
print(k2)
print(k3)