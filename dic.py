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
# v = int(input("Qaysi variantni tanlaysiz 1-2: "))
if qiymat.lower() == "samsung":
  #  print("Siz",brendlar["samsung"],"ni tanladingiz")
    print(brendlar["samsung"]["a"][0])
# elif qiymat.lower() == "huawei" :
#     print(brendlar["huawei"])

# elif qiymat.lower() == "apple":
#     print(brendlar["Apple"])

else:
    print("Bunaqa brend yo`q")


