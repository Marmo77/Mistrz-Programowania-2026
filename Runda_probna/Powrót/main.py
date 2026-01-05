# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r0a/

class Powrot:
    # 3 dni nieobecnosci -> 4 dzialy
    # dzialanie: proporcjonalnosc -> n / 3 = x | x * 4 = result
    # jesli wychodzi forma ulamkowa 14.66 to zaokraglenie w dol -> 14
    def do_nadrobienia(n: int) -> float: # n - ilosc dni nieobecnych
        # skala 3:4 podane jako zadanie

        dzialy_do_nadrobienia = (4 * n) // 3 # liczba n mnozona przez 4 i dzielona przez 3 bez reszty zokraglana w dol ( // )

        return dzialy_do_nadrobienia # zwraca wynik

if __name__ == "__main__":
    n = int(input())

    zadanie = Powrot.do_nadrobienia(n)
    print(zadanie)