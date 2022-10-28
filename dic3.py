oziq_ovqat = {
    "mevalar": "olma, anor,nok",
    "sabzavotlar": "sabzi, pomidor, bodring",
    "poliz_ekn": "qovoq, qovun,tarvuz"
}
v = input('''Oziq ovqatlardan birini tanlang:
mevalar
sabzavotlar
poliz
Qaysi birini tanlaysiz: ''')

if v.lower() == "mevalar":
    print(oziq_ovqat["mevalar"])
    for i in range(1,10,3):    
        print(i)
        
s = 0
if v.lower() == "sabzavotlar":
    print(oziq_ovqat["sabzavotlar"])
    while s<20:
        s += 1    
    print(s)
        
def poliz_ekn():
    if v.lower() == "poliz":
        print(oziq_ovqat["poliz_ekn"])

    else:
        print()
poliz_ekn()
