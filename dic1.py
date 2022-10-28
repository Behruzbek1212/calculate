brendlar = {
    "samsung": {
        "a": ["S22 ultra","900$"],
        "b": ["note20 plus","800$"]
        },
    
   "huawei": {
        "s":["Huawei p50 pro","700$"],
        "d":["Huawei p40","450$"]
       },

    "Apple": {
        "e": ["14 pro max 256 gb","1700$"],
        "f": ["MackBook Pro ultra pultra","11000$"]
    }


}
qiymat = input("Qaysi brendni tanlaysiz: ")
v = int(input("Qaysi variantni tanlaysiz 1-2: "))
if qiymat.lower() == "samsung" and v == 1:
    print("Siz",brendlar["samsung"],"ni tanladingiz")
    print(brendlar["samsung"]["a"])
elif qiymat.lower() == "samsung" and v == 2:
    print(brendlar["samsung"])
    print(brendlar["samsung"]["b"])


elif qiymat.lower() == "huawei" and v == 1:
    print(brendlar["huawei"])
    print(brendlar["huawei"]["s"])
elif qiymat.lower() == "huawei" and v == 1:
    print(brendlar["huawei"])
    print(brendlar["huawei"]["d"])

elif qiymat.lower() == "apple" and v == 1:
    print(brendlar["Apple"])
    print(brendlar["Apple"]["e"])
elif qiymat.lower() == "apple" and v == 1:
    print(brendlar["Apple"])
    print(brendlar["Apple"]["f"])

else:
    print("Bunaqa brend yo`q")
