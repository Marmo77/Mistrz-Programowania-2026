# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r0b/

class U_mnie_dziala:

    def liczby_parzyste(self, n: int) -> list[int]:
        liczby_parzyste: list[int] = []
        liczba = 1  # (1 ≤ 𝑛 ≤ 1000) - podany zakres liczby
        while len(liczby_parzyste) < n: # do momentu az znajdzie n liczb parzystych
            if liczba % 2 == 0:
                liczby_parzyste.append(liczba) # dodaje liczbe parzysta do listy
            liczba += 1

        # print(liczby_parzyste)
        return liczby_parzyste # zwraca liste liczb parzystych o dlugosci n

    def haslo_do_wifi(self, liczby_parzyste: list[int]):
        # 2 -> ilosc powtorzen 1
        # 4 -> ilosc powtorzen 3
        # k -> ilosc powtorzen k-1
        # ----
        # -- JEST DO DOBRE RÓWNIEŻ DOBRE ROZWIĄZANIE, ale nie jest efektywne i przekracza limit runtime error, limit konwersji do int jest 4300, wiec zwracamy haslo jako string --
        haslo = []
        for k in liczby_parzyste: # przechodzi przez każdy element list (dlugosc listy - n)
            ilosc_powtorzen = k - 1
            for _ in range(ilosc_powtorzen): # _ - zmienna tymczasowa (nie jest wykorzystywana)
                haslo.append(str(k)) # dodajemy liczby do hasla tyle razy ile -> k - 1 (mozna rowniez jako haslo += ale wtedy haslo: string)

        res = "".join(haslo) # haslo jako string | limit konwersji do int jest 4300, wiec zwracamy haslo jako string
        # ----
        return res # zwraca haslo





if __name__ == "__main__":
    n = int(input())

    zadanie = U_mnie_dziala()
    parzyste = zadanie.liczby_parzyste(n)
    haslo = zadanie.haslo_do_wifi(parzyste)
    print(haslo)
    
