#Usa un dizionario per contare quante volte appare ogni lettera in una stringa.
#Esempio:conta_lettere("banana") → `{'b': 1, 'a': 3, 'n': 2}`

#Creo un dizionario per salvare tutte le lettere (esiste la versione 2 dove le allocco dinamicamente; 
#i caratteri speciali si potrebbero aggiungere, ma ho deciso di evitarli per non appesantire la pagina).
class Dizionario:
    def __init__(self):
        self.dizionario_lettere={chr(lettera): 0 for lettera in range(97 , 123)}
        pass

#Creo la funzione nella quale prendo in input il dizionario e la parola inserita
    def contaLettere(self,parolaInserita):
        #converto tutte le lettere della parola in lettere minuscole
        parolaInserita=parolaInserita.lower()

        #Scorro la parola come se fosse un array e contemporaneamente controllo se la lettera si trova nel dizionario , se si la aggiorno
        for i in parolaInserita:
            if i in self.dizionario_lettere:
                self.dizionario_lettere[i]=self.dizionario_lettere[i]+1
                #ritorno il dizionario
        return self.dizionario_lettere
#Creo la funzione per acquisire una stringa dal CLI, non serve che stia nella classe e quindi l'ho messa assestante     
def inserisci_parola():
    parolaInserita=input("inserisci una stringa e ti stampero un dizionario indicandoti quali lettere contiene(escludendo i caratteri speciali) \n")
    return parolaInserita



oggetto_dizionario=Dizionario()
inserito=inserisci_parola()
oggetto_dizionario.contaLettere(inserito)
print(oggetto_dizionario.dizionario_lettere)

