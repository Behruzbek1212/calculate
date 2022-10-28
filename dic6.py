xislatlar = {
    "yaxshi": "rostgo`ylik, mehribonlik, hurmatli bo`lish...",
    "yomon": "yolg`onchilik, birovni ustidan kulish , kamsitish..."
}
qiymat = input('''Sizga qanday xislatlar yoqadi:
yaxshi
yomon
Tanlang: ''')
if qiymat.lower() == "yaxshi":
    print(xislatlar["yaxshi"])
elif qiymat.lower() == "yomon":
    print(xislatlar["yomon"])
else:
    print("Bunqa xislat topilmadi")