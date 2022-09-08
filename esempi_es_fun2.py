# scrivere una funzione che prenda due liste e restituisca la 
# lista con la somma elemento per elemento (se sono lunghe uguali, altrimenti 0)

# [2, 3, 4] [1, 2, 3] -> [3, 5, 7]

def somma_liste(l1, l2):
    if len(l1) == len(l2):
        lista_somma = []
        for i in range(len(l1)):
            lista_somma.append(l1[i] + l2[i])
        return lista_somma
    else:
        return 0

print(somma_liste([1], [2,3,4,5]))

print(somma_liste([1,2,0,3], [2,3,4,5]))