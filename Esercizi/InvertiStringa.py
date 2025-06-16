class Stringa():
    def __init__(self):
        self.stringaInserita=""
        self.stringaInvertita=""


    def inserisci(self):
        self.stringaInserita=input("inserisci una stringa che vuoi invertire\n")
        return self.stringaInserita

    def inverti(self):
        for i in self.stringaInserita:
            self.stringaInvertita=i+self.stringaInvertita
        return self.stringaInvertita


oggettoStringa=Stringa()
oggettoStringa.inserisci()
oggettoStringa.inverti()
print("la stringa che hai inserito invertita è :"+oggettoStringa.stringaInvertita)




