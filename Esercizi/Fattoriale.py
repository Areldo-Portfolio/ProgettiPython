#Scrivi una funzione che calcoli il fattoriale di un numero `n`.  
#Esempio: `fattoriale(5)` → `120`  

#definisco la funzione fattoriale che mi calcoli il fattoriale , ho creato la variabile numero1 da poter usare nella funzione , l'input viene preso da tastiera nel codice 
def fattoriale(numero):
    numero1=numero-1
    while numero1 >0:
        numero*=numero1
        numero1-=1
    return numero

print ("dammi un numero intero e ne estrarò il fattoriale")
numero=int(input())
numerofattoriale=fattoriale(numero)
print(numerofattoriale)

