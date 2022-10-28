a = int(input("1-son: "))
b = int(input("2-son: "))
amal = input("Amalni kiriting: ")
s = 0

def kalkulyator(a,b):
    if amal == "+":
        d=a+b
        print(d)
        while s < d:
            s += 1
            
            print(s)
    elif amal == "-":
        print(a-b)
        while s < (a+b):
            s += 1
            print(s)
    elif amal == "*":
        print(a*b)
        while s < (a+b):
            s += 1
            print(s)
    elif amal == "/":
        print(a/b)
        while s < (a/b):
            s += 1
            print(s)
    else:
        print("Xato amal kiritdingiz!")
kalkulyator(a,b)
