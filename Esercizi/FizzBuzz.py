#Stampa i numeri da 1 a 100, ma:  
#- Se un numero è **multiplo di 3**, stampa `"Fizz"`  
#- Se è **multiplo di 5**, stampa `"Buzz"`  
#- Se è **multiplo di entrambi**, stampa `"FizzBuzz"`  
#Esempio: `fizzbuzz()` stampa:  
#1
#2
#Fizz
#4
#Buzz
#Fizz

def fizzbuzz():
    for valore in range(1,101):
        if valore%5==0 and valore%3==0:#avrei potuto mettere una sola condizione con valore%15==0, ma ho preferito lasciarlo cosi 
            print("FizzBuzz")
        elif valore%5==0 and valore%3!=0:
            print("Buzz")
        elif valore%3==0 and valore%5!=0:
            print("Fizz")
        #conversto il valore in stringa per poterlo stampare     
        else: print(str(valore))


fizzbuzz()

