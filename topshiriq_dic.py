mashinalar = {
    "bmw":{
        "bmwlux":  ["Siz  BMW x6 ni tanladingiz. Narxi  150000$ dollr"],
        "bmw": ["Siz BMW x5 tanlafingiz. Narxi  100500$ dollr"]
    },
    "mersdes": {
        "merslux":  ["Siz Merdes 255g ni tanladingiz. Narxi  250000$ dollr."],
        "mers": ["Siz Mersdes 225s ni tanladingiz. Narxi 150000$ dollr."]
    },
    "tayota":  { 
        "tayotasport":["Narxi Supra turbo ni tanladingiz. Narxi 200000$ dollr."],
        "tayotaprodo": ["Siz Prodo ni tanladingiz. Narxi 65000$ dollr."]
    }
}
var = input('''BMW
Mersdes
Tayota
Qaysi mashinani tanladingiz: ''')

if var.lower() == "bmw" :
    print(mashinalar["bmw"])
qiy = int(input("Qaysi variantni tanlaysiz: 1 and 2 "))
if var.lower() == "bmw"  and qiy == 1:
    print(mashinalar["bmw"]["bmwlux"])
elif var.lower() == "bmw"  and qiy == 2:
    print(mashinalar["bmw"]["bmw"])

else:
    print()

if var.lower == "Mersdes":
    print(mashinalar["mers"])
#qiy2 = input("Qaysi variantni tanlaysiz: a and b ")
if var.lower == "Mersdes" and qiy == 1:
    print(mashinalar["mersdes"]["merslux"])
elif var.lower == "Mersdes" and qiy == 2:
    print(mashinalar["mersdes"]["mers"])
else:
    print()
    

if var.lower() == "Tayota":
    print(mashinalar["tayota"])
#qiy3 = input("Qaysi variantni tanlaysiz: e and f ")
if var.lower() == "Tayota" and qiy == 1:
    print(mashinalar["tayota"]["tayotasport"])
elif var.lower() == "Tayota" and qiy == 2:
    print(mashinalar["tayota"]["tayotaprodo"])

else:
    print()
