try:
    import time
    log = input("Loginni kiriting: ")
    par = int(input("Parolni kiriting: "))

    if log != "begi" and par != 1212:
        s = 0
        while s < 60:
            s += 1
            time.sleep(1)
            print(s)
    elif log == "begi" and par == str:
        print("parol xato")

    elif log == "begi" and par != 1212:
        a = 0
        while a < 10:
            a += 1
            time.sleep(1)
            print(a)

    else:
        print("Kirishingiz mumkin")
except:
    print("Siz str kiritdingiz")