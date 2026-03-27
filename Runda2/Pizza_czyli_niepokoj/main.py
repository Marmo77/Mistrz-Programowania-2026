class PizzaCzyliNiepokoj:
    
    def wartoscSmakowe(self, n, k):
        
        wartosci_smakowe = list(map(int, input().split()))
        print(wartosci_smakowe)
        # wartosci_smakowe = (int(x) for x in wartosci_smakowe)

        aktualna_wartosc = 0
        for i in range(k):
            aktualna_wartosc += wartosci_smakowe[i]

        najlepszy_wynik = aktualna_wartosc
            # print(aktualna_wartosc)
        print('----')
        
        najmniejsza_pref =0

        suma_pref = 0

        # sprawdza wszystkie kolejne pizze
        for i in range(k,n):

            #pizza na prawo
            aktualna_wartosc += wartosci_smakowe[i]

            suma_pref += wartosci_smakowe[i-k]
            
            if suma_pref < najmniejsza_pref:
                najmniejsza_pref = suma_pref

            # jesli jest lepiej nadpisz naj. wynik
            if aktualna_wartosc - najmniejsza_pref > najlepszy_wynik:
                najlepszy_wynik = aktualna_wartosc - najmniejsza_pref
        
        return najlepszy_wynik

if __name__ == "__main__":

    wejscie = input()

    n,k = map(int, wejscie.split(' '))

    pizza = PizzaCzyliNiepokoj()
    print(pizza.wartoscSmakowe(n, k))

