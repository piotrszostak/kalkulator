import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    return a + b
    
ask = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n"))

a1 = float(input("podaj pierszy składnik:\n"))
a2 = float(input("podaj drugi składnik:\n"))

if ask == 1:
    logging.info(f"Dodaję {a1} oraz {a2}.")
    print(add(a1,a2))
elif ask == 2:
    pass
elif ask == 3:
    pass
elif ask == 4:
    pass