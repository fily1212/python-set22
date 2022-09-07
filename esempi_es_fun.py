# Definire le funzioni della calcolatrice in notazione polacca inversa
# 5 6 + =     11
# 5 3 * =     15
# 10 5 - =    5
# 10 10 5 * - =  -40 

def somma():
    n1 = lista_numeri.pop()
    n2 = lista_numeri.pop()
    lista_numeri.append(n1 + n2)

def stampa():
    print(lista_numeri)


s = input("Inserisci l'espressione in notazione polacca inversa terminata da = ")
s = s.split(" ")

lista_numeri = []

for elem in s: 
    if elem == '+':
        somma()
    elif elem == '-':
        sottrazione()
    elif elem == '*':
        moltiplicazione()
    elif elem == '/':
        divisione()
    elif elem == '=':
        stampa()
    else: 
        lista_numeri.append(float(elem))
