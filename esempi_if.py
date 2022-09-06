# Chiediamo a un utente un numero, stampare se è negativo, positivo o = 0
n = int(input("Inserisci un numero: "))
if n > 0:
    print("È positivo")
elif n == 0:
    print("È zero")
else:
    print("È negativo")

'''
Base: chiedere all'utente tre angoli di un triangolo e dire se può esserlo
se la somma degli angoli è 180°

PRO: Chiedere tre lati e dire se è equilatero, isoscele, scaleno

Inserire due nomi e stampare il nome più lungo
'''

a = int(input("Inserisci un angolo: ")) 
b = int(input("Inserisci un angolo: ")) 
c = int(input("Inserisci un angolo: ")) 
if a+b+c == 180:
    print("È un triangolo")
else: 
    print("No")

print("È un triangolo" if a+b+c == 180 else "No")
a = "È un triangolo" if a+b+c == 180 else "No"
print(a)

# OPERATORE TERNARIO
# valore true if condizione else valore false

a = int(input("Inserisci un lato: ")) 
b = int(input("Inserisci un lato: ")) 
c = int(input("Inserisci un lato: ")) 
if a == b and a == c : 
    print("Equilatero")
elif a != b and a != c and b != c:
    print("Scaleno")
else:
    print("Isoscele")

n1 = input("Nome: ")
n2 = input("Nome: ")
if len(n1) > len(n2):
    print(n1)
else:
    print(n2)

print(n1 if len(n1) > len(n2) else n2)
