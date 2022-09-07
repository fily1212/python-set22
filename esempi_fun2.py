# funzione che ritorna il massimo degli elementi della lista al quadrato
# ESEMPIOINPUT[-2, 0, 1] : OUTPUT -2 (4)


def riempi_lista(lunghezza):
    lista = []
    for i in range(lunghezza):
        lista.append(int(input("Inserisci un numero: ")))
    return lista

def massimo_strano(lista):
    posizione_max_quadrato = 0
    for i in range(len(lista)):
        if lista[i]**2 > lista[posizione_max_quadrato] ** 2:
            posizione_max_quadrato = i
    return lista[posizione_max_quadrato]

a = riempi_lista(5)
print(massimo_strano(a))

