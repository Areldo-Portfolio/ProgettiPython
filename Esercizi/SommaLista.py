"""**Somma degli elementi in una lista**  
Scrivi una funzione che calcoli la somma di tutti gli elementi di una lista.  
```python
def somma_lista(lista):
    pass  # Completa la funzione
```
**Esempio**: `somma_lista([1, 2, 3])` → `6`"""


class Sommatore():
    def __init__(self):
        #dichiaro una lista
        self.assegnatore=[ i for i in range(0,6)]
    #stampo l'oggetto assegnatore
    def stampa(self):
        print(self.assegnatore)
        pass
    # definisco un counter nella quale sommare gli elementi della lista assegnatore
    def sommatoria(self):
        sommatoria=0
        for i in self.assegnatore:
            sommatoria=sommatoria+i
        return sommatoria




oggetto_Sommatore=Sommatore()
oggetto_Sommatore.stampa()
daStamp=oggetto_Sommatore.sommatoria()
print('il risultato della sommatoria è: '+str(daStamp))
