komlar = {
    "lenovo": "ozu-4, pamyt-556 gb",
    "macbook": "ozu-16, pamyt-1 tr",
    "asus": "ozu-8, pamyt-556 gb"

}
qiymat = input('''lenovo
macbook
asus
Qaysi kompni tanlaysiz: ''')
if qiymat.lower() == "lenovo":
    print(komlar["lenovo"])

elif qiymat.lower() == "macbook":
    print(komlar["macbook"])
    
elif qiymat.lower() == "asus":
    print(komlar["asus"])
else:
    print("Bunaqa komp yo`q")