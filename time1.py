import time

a = int(input("Parolni kiriting: "))
if a == "1212":
    print("Kod tasdiqlandi")
else:    
    s = 0
    while s < 60:
        s += 1
        time.sleep(1)
        print(s)
        
