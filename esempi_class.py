class Persona:
    # il costruttore è un metodo che descrive 
    # che cosa succede quando creo l'oggetto
    def __init__(self, nome):
        self.nome = nome
    
    def stampa(self):
        print(self.nome)

lara = Persona('Lara')
zeno = Persona('Zeno')
lara.stampa()
zeno.stampa()


#Persona.stampa(lara)