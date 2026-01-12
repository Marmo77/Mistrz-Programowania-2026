class Kurtka:
    pass
    def czy_kurtka_jest_bezpieczna(self, n, a, b, c) -> str: # n jest nam nie potrzebne

        dotyka = False

        if c >= a and c <= b: # jesli c znajduje sie w przedziale a-b np. (a=6, b=10, c=8 - jest w przedziale)
            dotyka = True

        if dotyka:
            return "Nie dotykaj mojej kurtki!"
        else:
            return "Spokojnie."
        
# 100 / 100

if __name__ == "__main__":

    powieszona_kurtka = input()
    
    n,a,b,c = map(int, powieszona_kurtka.split()) # n -> ilosc haczykow, a - b -> karol zajmuje haczyki od a do b, c -> agent kombinuje przy tym haczyku

    kurtka = Kurtka()
    print(kurtka.czy_kurtka_jest_bezpieczna(n, a, b, c))

