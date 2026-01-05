# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r1b/

# class Maksimum_czy_minimum:

#     def maksimum(self, n: int) -> int: # n - liczba druzyn (2 ≤ 𝑛 ≤ 105)
#         druzyny: dict[int, dict[int, int]] = {} # pierwszy i - {id_druzyny}, drugi dict z {liczba_zadan, kara_czasowa}
#         i: int = 0
#         while len(druzyny) < n: # do momentu az bedzie tyle samo elementow co n
#             odczytaj = input() 
#             podzial = odczytaj.split(' ') #dzielimy input na dwie czesci -> 2 4 = [2, 4]
#             druzyny[i] = { # z - zrobione zadania, t - kara czasowa
#                 'z': int(podzial[0]), 
#                 't': int(podzial[1])
#             } # tworzymy slownik z id_druzyny i {liczba_zadan, kara_czasowa}

#             i += 1 #zwiekszamy index nastepnej druzyny o 1
        
#         najw_zadan = 0 # najwieksza liczba zadan

#         for druzyna in druzyny.values(): # przechodzimy przez wszystkie druzyny 
#             if druzyna['z'] > najw_zadan: # jesli liczba zadan jest wieksza niz najw_zadan to je ustawiamy
#                 najw_zadan = druzyna['z']

#         ilosc_najwiekszych = 0 # ilosc druzyn z najwieksza liczba zadan (jesli > 1 to patrzymy ktora ma mniejsza kare czasowa)
#         for druzyna in druzyny.values(): 
#             if druzyna['z'] == najw_zadan: # jesli liczba zadan druzyny jest rowna najw_zadan to zwiekszamy ilosc_najwiekszych o 1
#                 ilosc_najwiekszych += 1
        
#         if ilosc_najwiekszych > 1: # jesli ilosc_najwiekszych jest wieksza niz 1 to znaczy ze musimy sprawdzic ktora ma najmniejsza kare czasowa 
#             return "MINIMUM" # chyba nie trzeba sprawdzac kary skoro wiemy ze liczba zadan nie byla priorytetem
#         else:
#             #i tutaj zwracamy metode MAKSIMUM -> czyli ze ilosc zadan byla priorytetem druzyny
#             return "MAKSIMUM"

# U GÓRY JEST POPRAWNY KOD, LECZ TRZEBA ZOPTYMALIZOWAĆ CZASOWO PONIEWAŻ ON DAJE NAM 98/100 pkt.
# ----------------------------------------------------------------------------------------------------
class Maksimum_czy_minimum:

    def maksimum(self, n: int) -> int: # n - liczba druzyn (2 ≤ 𝑛 ≤ 105)
        druzyny: dict[int, int] = {} # pierwszy i - {id_druzyny}, drugi dict z {liczba_zadan, kara_czasowa}
        i: int = 0
        while len(druzyny) < n: # do momentu az bedzie tyle samo elementow co n
            odczytaj = input() 
            #dzielimy input na dwie czesci -> 2 4 = [2, 4]
            druzyny[i] = int(odczytaj.split(' ')[0])
            i += 1 #zwiekszamy index nastepnej druzyny o 1
        
        najw_zadan = 0 # najwieksza liczba zadan

        for druzyna in druzyny.values(): # przechodzimy przez wszystkie druzyny 
            if druzyna > najw_zadan: # jesli liczba zadan jest wieksza niz najw_zadan to je ustawiamy
                najw_zadan = druzyna

        ilosc_najwiekszych = 0 # ilosc druzyn z najwieksza liczba zadan (jesli > 1 to patrzymy ktora ma mniejsza kare czasowa)
        for druzyna in druzyny.values(): 
            if druzyna == najw_zadan: # jesli liczba zadan druzyny jest rowna najw_zadan to zwiekszamy ilosc_najwiekszych o 1
                ilosc_najwiekszych += 1
        
        if ilosc_najwiekszych > 1: # jesli ilosc_najwiekszych jest wieksza niz 1 to znaczy ze musimy sprawdzic ktora ma najmniejsza kare czasowa 
            return "MINIMUM" # chyba nie trzeba sprawdzac kary skoro wiemy ze liczba zadan nie byla priorytetem
        else:
            #i tutaj zwracamy metode MAKSIMUM -> czyli ze ilosc zadan byla priorytetem druzyny
            return "MAKSIMUM"

# KOD KTÓRY NIE BIERZE CZASU POD UWAGE PONIEWAZ DO POPRWANOSCI ZADANIE NIE JEST ON NAM POTRZEBNY
# ----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    n = int(input())

    zadanie = Maksimum_czy_minimum()
    print(zadanie.maksimum(n))
