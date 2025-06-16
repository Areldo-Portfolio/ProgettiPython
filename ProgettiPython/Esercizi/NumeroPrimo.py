"""**Numeri primi**  
Scrivi una funzione che controlli se un numero è primo.  
```python
def è_primo(n):
    pass  # Completa la funzione
```
**Esempio**: `è_primo(7)` → `True`"""

def è_primo(n):
    if n <= 1:  #controllo se parte è maggiore di 1
        return False
    for i in range(2, n):  # Controlla i divisori da 2 a n-1
        if n % i == 0:  # Se il numero è divisibile per qualsiasi numero in questo range, non è primo
            return False
    return True  # Se non ha trovato divisori, è primo

# Uso della funzione
print("Dammi un numero")
numero = int(input())

if è_primo(numero):
    print("Il numero è primo")
else:
    print("Il numero non è primo")
