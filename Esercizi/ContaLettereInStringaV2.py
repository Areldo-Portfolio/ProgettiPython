#Usa un **dizionario** per contare quante volte appare ogni lettera in una stringa.  
#Esempio: `conta_lettere("banana")` → `{'b': 1, 'a': 3, 'n': 2}`
#questa è la seconda versione del contalettere

#Creo il dizionario , questa volta vuoto
class Dizionario:
    def __init__(self):
        self.dizionario_lettere={}
        pass

    #definisco la funzione contalettere
    def contaLettere(self,parolaInserita):
        #trasformo tutte le lettere inserite in minuscole
        parolaInserita=parolaInserita.lower()
        #scorro la parola inserita come se fosse un array
        for i in parolaInserita:
            #se la parola non è nel dizionario la inserisco e le assegno il valore 1
            if i not in self.dizionario_lettere:
                self.dizionario_lettere[i]=1
            #Se la parola è nel dizionario, incremento il valore associato alla chiave    
            if i in self.dizionario_lettere:
                self.dizionario_lettere[i]=self.dizionario_lettere[i]+1
                #ritorno il dizionario
                return self.dizionario_lettere

def inserisci_parola():
    parolaInserita=input("inserisci una stringa e ti stampero un dizionario indicandoti quali lettere contiene(escludendo i caratteri speciali) \n")
    return parolaInserita



oggetto_dizionario=Dizionario()
inserito=inserisci_parola()
oggetto_dizionario.contaLettere(inserito)
print(oggetto_dizionario.dizionario_lettere)