import logging 
logging.basicConfig(level=logging.INFO) 

def add(a, b): 
    return a + b 

def sub(a, b): 
    return a - b 

def mul(a, b): 
    return a * b 

def div(a, b): 
    return a / b 

ask = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n")) 

num1 = int(input("podaj pierszy składnik:\n")) 
num2 = int(input("podaj drugi składnik:\n")) 

if ask == 1: 
    logging.info(f"Dodaję {num1} oraz {num2}.") 
    print(add(num1,num2)) 
elif ask == 2: 
    logging.info(f"Od {num1} odejmuję {num2}.") 
    print(sub(num1,num2)) 
elif ask == 3: 
    logging.info(f"Mnożę {num1} razy {num2}.") 
    print(mul(num1,num2)) 
elif ask == 4: 
    logging.info(f"Dzielę {num1} przez {num2}.") 
    print(div(num1,num2))