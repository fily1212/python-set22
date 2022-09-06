c = 0
a = ['elem1', c, 'elem3']
b = []
a[2] = 'elem nuovo'
matrice =  [['x',' ',' '],
            ['x','o','o'],
            ['x',' ','o']]
print(len(matrice))
# creare una lista di 2 numeri e calcolare la media dei numeri
#a = [ 0, 1]
nomi = ["Marco", "Zeno", "Lara"]
#media = (a[0] + a[1]) / 2
print(nomi)
# aggiungere un elemento alla lista
nomi.append("Antonio")
print(nomi)
# rimuovere un elemento dalla lista
nomi.remove("Marco")
print(nomi)
# inserire in una posizione 
nomi.insert(1,"Clelia")
print(nomi)
# rimuovere ( eventualmente in una posizione) ritornando il valore
print(nomi.pop())
print(nomi)
print(nomi.pop(0))
print(nomi)
# esempio di errore, indice fuori dal range
# print(nomi.pop(2))
print("Zeno" in nomi)
print("Lara" in nomi)
not "Lara" in nomi
"Lara" not in nomi
print(nomi)
''' creare una lista di nomi, chiedere all'utente di inserire 5 nomi 
 e inserirli nella lista solo se sono nomi nuovi '''
#for elem in range(5):
#    s = input("Inserisci un nome: ")
#    if s not in nomi:
#        nomi.append(s)
#    print(nomi)

for nome in nomi:
    print(nome + "\n")

# Stampare i numeri da 0 a 10
for elem in range(11):
    print(elem)

for elem in [0,1,2,3,4,5,6,7,8,9,10]:
    print(elem)


