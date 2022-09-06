''' chiedere all'utente quanti voti di matematica vuole inserire, 
salvarli in una lista e calcolare: 
min, massimo, media
''' 
num = int(input("Quanti voti vuoi inserire? "))
voti = []
for i in range(num):
    print(i)
    voti.append(int(input("Voto " + str(i+1) + ": ")))
print(voti)

min = voti[0]
for voto in voti:
    if voto < min:
        min = voto
print(min)

for lettera in 'CIAO':
    print(lettera)
# stampare le vocali del proprio nome
