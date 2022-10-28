mashina = {
    "BMW": ["model: bmw x7","narxi: 150000$"],
    "Mersdes": ["model: mersdes s250","narxi: 250000$"],
    "Tayota": ["nomi: Supra","narxi: 250000$"]

}
v = int(input('''Qaysi mashinani tanlaysiz:
1-BMW:,
2-Mersdes:,
3-Tayota:
'''))
if v == 1:
    print(mashina["BMW"])
elif v == 2:
    print(mashina["Mersdes"])
elif v == 3:
    print(mashina["Tayota"])
else:
    print("Bunaqa mashina turi yo`q")