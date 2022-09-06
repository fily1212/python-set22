''' chiedere all'utente quanti voti di matematica vuole inserire, 
salvarli in una lista e calcolare: 
min, massimo, media
''' 
num = int(input("Quanti voti vuoi inserire? "))
voti = []
for i in range(num):
    voti.append(int(input("Voto " + str(i+1) + ": ")))
print(voti)
