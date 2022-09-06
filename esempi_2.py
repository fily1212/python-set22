# Chiediamo all'utente la media dei voti di Matematica e Italiano. 
# Salviamo (e stampiamo)
# in una variabile promosso se entrambe sono sufficienti (>=6) .
#m = int(input("Inserisci il voto di Matematica: "))
#i = int(input("Inserisci il voto di Italiano: "))
#promosso = m >=6 and i >= 6
#print(promosso) 

''' chiediamo all'utente un anno e stampiamo True se è bisestile false altrimenti
 Un anno è bisestile se è divisibile per 4 e non per 100 o 
 se è divisibile per 400
 2020: True
 1900: False
 2022: False
 2000: True'''
anno = int(input("Inserisci un anno: "))
bisestile = (anno % 4 == 0 and (not anno % 100 == 0)) or anno % 400 == 0
#print("Anno bisestile: " + str(bisestile))

#(anno % 4 == 0)

'''if [condizione]:
    istruzione 1
    istruzione 2
istruzione fuori dall'if

if (condizione){
    istruzione 1
    istruzione 2
}
istruzione fuori'''
if bisestile:
    print("È bisestile")
else: 
    print("Non è bisestile")    
print("Ciao")
