# stampare i numeri da 1 a 10
i = 0
while i < 10:
    print(i + 1)
    i = i + 1

# chiedere all'utente una lista di nomi, smettere quando inserisce 0

nome = input("inserisci un nome: ")
nomi = []
while nome != '0':
    nomi.append(nome)
    nome = input("inserisci un nome: ")

print(nomi)

# far inserire all'utente una lista di voti e calcolare la media 
# smettere quando mette un numero negativo

somma = 0
nvoti = 0
voto = int(input("Inserisci un voto: "))
while voto >= 0 :
    somma += voto
    nvoti += 1
    voto = int(input("Inserisci un voto: "))
media = somma / nvoti
print(media)

numeri = [5,6,7,8,9,10]


numeri_pari = []
for numero in numeri:
    if numero % 2 == 0:
        numeri_pari.append(numero)

# list comprehension
numeri_pari = [numero for numero in numeri if numero % 2 == 0]
print(numeri_pari)

