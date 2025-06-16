#Scrivi una funzione che accetti una stringa e restituisca il numero di vocali (a, e, i, o, u).  
#Esempio: `conta_vocali("ciao")` → `2`  

#Creo la classe vocali, all'interno inizializzo la lista di vocali e il dizionario di vocali
class Vocali:
    def __init__(self):
        self.vocali=['a','e','i','o','u']
        self.dizionarioVocali={'a':0,'e':0,'i':0,'o':0,'u':0}

    #definisco la funzione contalettere che prende in input self e la frase inserita da input
    def contatoreDiLettere(self,frase):
        #controllo se c'è la lettera nella frase , se c'è incremento la valore associato alla chiave dizionario di 1
        for lettera in frase:
            if lettera in self.vocali:
                self.dizionarioVocali[lettera]+=1
        return  self.dizionarioVocali   
    



#creo l'oggetto_vocali per poter accedere allaclasse Vocali
oggetto_vocali=Vocali()
frase=input("inserisci una frase\n").lower()
#passo alla funzione contatoreDiLettere che sei trova in Vocali la frase presa di input
#creo e salvo in risultato l'output della funzione
risultato=oggetto_vocali.contatoreDiLettere(frase)
lettera=input("inserisci una vocale\n").lower()
#controllo se ha inserito una vocale o più lettere
if lettera not in oggetto_vocali.vocali or len(lettera)!=1:
    print("non hai inserito una vocale")
else:
#stampo la lettera e il numero di volte che è appare
    print('Hai inserito la vocale ' + lettera + ' ed è apparsa ' + str(risultato[lettera]) + ' volte')


