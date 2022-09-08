class Bottiglia:
    def __init__(self, capacita, quantita):
        self.c = capacita
        self.q = quantita
    
    def __str__(self):
        return "Bottiglia - capacità: " + str(self.c) + \
        " - quantità: " + str(self.q)
    def riempi(self, q):
        # se la q è negativa voglio che si riempa di 0
        # se straborda viene riempita fino all'orlo
        if q > 0:
            if self.q + q > self.c : 
                self.q = self.c
            else: 
                self.q += q
        #
        if q > 0: 
            self.q = min(self.q + q, self.c)
    
    def svuota(self, q):
        if q > 0:
            self.q = max(self.q - q, 0)

# Una sottoclasse è una classe che eredità le proprietà della classe genitore
class BottigliaConTappo(Bottiglia):
    def __init__(self, q, c):
        self.aperta = True
        super().__init__(q, c)
    
    def riempi(self, q):
        if self.aperta:
            super().riempi(q)

    def svuota(self, q):
        if self.aperta:
            super().svuota(q)

    def apri(self):
        self.aperta = True
    
    def chiudi(self):
        self.aperta = False

    def __str__(self):
        return "Bottiglia - capacità: " + str(self.c) + \
        " - quantità: " + str(self.q) + " aperta: " + str(self.aperta)
        

a = Bottiglia(750,500)
print(a)
a.riempi(1000)
print(a)
a.svuota(2200)
print(a)
b = BottigliaConTappo(1000, 500)
print(b)
b.svuota(100)
print(b)
b.chiudi()
print(b)
b.svuota(100)
print(b)