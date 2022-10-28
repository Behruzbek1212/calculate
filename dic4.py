fasllar = {
    "qish": {
        "oy1":  ["dekabr"],
        "oy2": ["yanvar"],
        "oy3":["fevral"]
    },
     "bahor": {
        "oy4": ["mart"],
        "oy5": ["aprel"],
        "oy6": ["may"]
    },
    "yoz": {
        "oy7": ["iyun"],
        "oy8": ["iyul"],
        "oy9": ["avgust"]
    },
    "kuz": {
        "oy10": ["sentabr"],
        "oy11":  ["oktabr"],
        "oy12": ["noyabr"]
    }
}

qiymat = input("Qaysi faslni tanlaysiz: ")
qiymat2 = int(input("Nechanchi oyi kerak: "))
if qiymat.lower() == "qish" and qiymat2 == 1:
    print(fasllar["qish"]["oy1"])
elif qiymat.lower() == "qish" and qiymat2 == 2:
    print(fasllar["qish"]["oy2"])
elif qiymat.lower() == "qish" and qiymat2 == 3:
    print(fasllar["qish"]["oy3"])
elif qiymat.lower() == "bahor" and qiymat2 == 1:
    print(fasllar["bahor"]["oy4"])
elif qiymat.lower() == "bahor" and qiymat2 == 2:
    print(fasllar["bahor"]["oy5"])
elif qiymat.lower() == "bahor" and qiymat2 == 3:
    print(fasllar["bahor"]["oy6"])
elif qiymat.lower() == "yoz" and qiymat2 == 1:
    print(fasllar["yoz"]["oy7"])
elif qiymat.lower() == "yoz" and qiymat2 == 2:
    print(fasllar["yoz"]["oy8"])
elif qiymat.lower() == "yoz" and qiymat2 == 3:
    print(fasllar["yoz"]["oy9"])
elif qiymat.lower() == "kuz" and qiymat2 == 1:
    print(fasllar["kuz"]["oy10"])
elif qiymat.lower() == "kuz" and qiymat2 == 2:
    print(fasllar["kuz"]["oy11"])
elif qiymat.lower() == "kuz" and qiymat2 == 3:
    print(fasllar["kuz"]["oy12"])