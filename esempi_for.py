''' chiedere all'utente quanti voti di matematica vuole inserire, 
salvarli in una lista e calcolare: 
min, massimo, media
''' 
num = int(input("Quanti voti vuoi inserire? "))
voti = []
for i in range(num):
    voti.append(int(input("Voto " + str(i+1) + ": ")))
print(voti)

if num > 0:
    min = voti[0]
for voto in voti:
    if voto < min:
        min = voto
print("min: " + str(min))

if num > 0:
    max = voti[0]
for voto in voti:
    if voto > max:
        max = voto
print("max: " + str(max))

media = 0
for voto in voti:
#    media = media + voto
    media += voto
if num > 0:
    media /= num
#media = media / num
print("media: " + str(media))

s = ''
for lettera in 'EDOARDO':
    if lettera in 'aeiouAEIOUòàèìùÈ':    
        s += lettera
        #s = s + lettera
print(s)
# stampare le vocali del proprio nome
