# definizione di funzione doppio
def doppio(n):
    return 2 * n



def riempi_lista(lunghezza):
    lista = []
    for i in range(lunghezza):
        lista.append(int(input("Inserisci un numero: ")))
    return lista

# chiamata della funzione doppio
print(doppio(5))
a = riempi_lista(3)
print(a)

# funzione che vuole in ingresso tre numeri e ritorna il massimo
def massimo(n1,n2,n3):
    #if n1 > n2:
    #    if n1 > n3:
    #        return n1
    #    else:
    #        return n3
    #else:
    #    if n2 > n3:
    #        return n2
    #    else:
    #        return n3
    
    #EQUIVALENTE
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(massimo(5,8,-2))