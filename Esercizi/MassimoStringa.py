""" **Trova il massimo in una lista**  
Scrivi una funzione che trovi il valore massimo in una lista.  
```python
def massimo(lista):
    pass  # Completa la funzione
```
**Esempio**: `massimo([3, 7, 2, 9])` → `9` """



class Numeri():
    def __init__(self):
    #dichiaro una lista vuota
        self.numeri=[]
#dichiaro una funzione che permetta all'usufruente del programma di assegnare la lista
    def assegna(self):
        i=0
        print("dammi un numero minore di 10 , finche sarà minore continuerò ad ampliare la lista aggiungendo gli elementi")
        while (i<=9):
            i=int(input())
            if i<=9:
                self.numeri.append(i)

    def trovaMaggiore(self):
        if not self.numeri:
            return ("la lista è vuota")
        maggiore=self.numeri[0]
        for i in  self.numeri:
            if i >maggiore:
                maggiore=i
        return maggiore
    def __str__(self):
        return str(self.trovaMaggiore())      

Oggetto_numeri=Numeri()
Oggetto_numeri.assegna()
print("il numero più grande della lista che hai inserito è: "+Oggetto_numeri.__str__())


