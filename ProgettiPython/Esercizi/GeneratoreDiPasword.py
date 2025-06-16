"""
**Genera una password casuale**  
Scrivi una funzione che generi una password casuale di `n` caratteri usando lettere e numeri.  
```python
import random
import string

def genera_password(n):
    pass  # Completa la funzione
```
**Esempio**: `genera_password(8)` → `"A7b3D2fG"`  """


import random
import string

class Password:
    def __init__(self):
        self.password=[]

    def creaPassword(self,lunghezza):
        while self.password.__len__()<lunghezza:
            numero=random.randint(0,2)
            if (numero==0):
                self.password.append(str(random.randint(0,9)))
            if (numero==1):
                self.password.append(chr(random.randint(97,123)))
            if (numero==2):
                self.password.append(chr(random.randint(65,91)))
        return "".join(self.password)    

                
   
oggetto_password=Password()
print("quanto vuoi che sia lunga la password?\n")
#chiedo quanto vuole che sia lunga la password
lunghezza_password=int(input())
password=oggetto_password.creaPassword(lunghezza_password)
print ("la password che ho creato per te è: "+password)