# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r1a/

import math

class Szklanka:

    def polowaSzklanki(self, h: int) -> int: # h - wysokosc szklanki
        result: float = h / 2 # dzielimy wysokosc szklanki na 2
        #----------
        # metoda 1 - z uzyciem if, jesli wynik zanizony jest mniejszy od wyniku to znaczy ze do koncowego wyniku musimy dodać 1, w przeciwnym wypadku zwracamy int(result)
        # if math.floor(result) < result:
        #     result = math.floor(result) + 1
        #     return result
        # else:
        #     return int(result)
        #----------
        
        # metoda 2 - z uzyciem math.ceil, jesli wynik ma cos po kropce to zaokragla w gore np. 7.3 -> 8
        return math.ceil(result)



if __name__ == "__main__":
    n = int(input())

    zadanie = Szklanka()
    print(zadanie.polowaSzklanki(n))