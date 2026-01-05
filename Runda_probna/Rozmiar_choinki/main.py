# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r0c/

class RozmiarChoinki:

    def rozmiar_choinki(self, n: int) -> int:
        # n -> ilosc choinek w sklepie
        # ? <liczba> -> zapytanie do systemu
        #  >,<,= -> odpowiedzi systemu

        # trzeba wykorzystac drzewo binarne - lewo, prawo
        lewo, prawo = 1, n # od skrajnie lewej do skrajnie prawej (cały zakres choinek)

        while lewo <= prawo: # do momentu az nie znajdzie odpowiedzi
            srodek = (lewo + prawo) // 2 # daje nam liczbe srodkowa bez reszty ( int )
            #teraz pytamy systemu o srodek (mniejsza czy wieksza czy rowna)
            print(f"? {srodek}", flush=True)
            odpowiedz = input() # teraz otrzymujemy odpowiedz i porownujemy
            if odpowiedz == "=":
                return srodek # znalezlismy liczbe i zwracamy
            elif odpowiedz == ">":
                lewo = srodek + 1 # przesuwamy naszą liczbę z lewej do tej środkowej + 1 (bo liczba jest wieksza niż srodek)
            else: # pozostale warunki (czyli "<")
                prawo = srodek - 1 # przesuwamy naszą liczbę z prawej do tej środkowej - 1 (bo liczba jest mniejsza niż srodek)

if __name__ == "__main__":
    n = int(input())

    zadanie = RozmiarChoinki()
    zadanie.rozmiar_choinki(n)