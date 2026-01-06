# ZADANIE -> https://szkopul.edu.pl/c/mistrz-programowania-2026/p/r1c/

class Praktyka_plus_teoria:
    
    # def moceElektrowni(self, n: int): #n - liczba elektrowni (2 ≤ 𝑛 ≤ 10^6)
    #     if n < 2 or n > 10**6:
    #         return []

    #     i = 0
    #     moce_elektrowni: list[int] = [] # lista z podstawowymi mocami elektrowni
    #     odpowiedz = input()
    #     while i < n: # przechodzi przez wszystkie elektrownie i dopisuje ich moc do listy moce_elektrowni
    #         moce_elektrowni.append(int(odpowiedz.split(' ')[i]))
    #         i += 1
        
    #     # teraz funkcjonalność
    #     elektrownie: list[int] = []
    #     for i in range(len(moce_elektrowni)): # przechodzimy przez wszystkie elektrownie
    #         balans_mocy = 0 # tworzymy zmienna balans_mocy
    #         for j in range(len(moce_elektrowni)):
    #             if i != j: # jesli i jest rozne od j to dodajemy do balans_mocy (czyli jesli i=0 to dodajemy do balans_mocy wszystkie elementy z moce_elektrowni poza pierwszym itd.)
    #                 balans_mocy += moce_elektrowni[j]

    #         elektrownie.append(balans_mocy) # dodajemy balans_mocy do listy elektrownie

    #     return " ".join(map(str, elektrownie))
# U GÓRY JEST POPRAWNY KOD, LECZ TRZEBA ZOPTYMALIZOWAĆ CZASOWO PONIEWAŻ ON DAJE NAM 60/100 pkt. i przekraczamy limity czasowe
# ----------------------------------------------------------------------------------------------------
# Zmiana podejścia do rozwiązania:
# 1. nie sprawdzamy odpoweidzi w kodzie tylko w "main'ie, i odrazu przekazujemy wartosci"
# 2. obliczamy całkowitą sumę mocy elektorowni
# 3. dla każdej elektrowni od sumy całkowitej odejmujemy moc danej elektrowni
# 4. dodajemy to do listy i zwracamy stringa

#--------------------------------
# dlaczego jest optymalniejsze:
# - Poprzedni kod liczył wszystko w funkcji, a teraz poza nią dzieje się wiele operacji (sumowanie i tworzenie listy),
# przez co nie trzeba wykorzystywac petli for kilkukrotnie w kodzie

    def moceElektrowni(self, n: int, moce_elektrowni: list[int], suma_mocy: int): #n - liczba elektrowni (2 ≤ 𝑛 ≤ 10^6)
        if n < 2 or n > 10**6:
            return

        elektrownie: list[int] = []
        for i in range(n):
            elektrownie.append(suma_mocy - moce_elektrowni[i])

        #---- zastosowano w mainie ----
        # suma = sum(moce_elektrowni) # suma wszystkich mocy elektrowni
        # for i in range(len(moce_elektrowni)): # dla kazdego elementu z elektrowni odejmujemy jego moc od sumy wszystkich elektrowni
        #     elektrownie.append(suma - moce_elektrowni[i]) # suma calkowita w przypadku (8 4 6 9 7) -> 34 - [i = 0] -> 34 - 8 = 26, wtedy nie trzeba przechodzic O(n^2)
        #------------------------------

        # # obliczanie mocy elektrowni
        # for i in range(len(moce_elektrowni)): # przechodzimy przez wszystkie elektrownie
        #     balans_mocy = sum(moce_elektrowni) - moce_elektrowni[i] # obliczamy balans_mocy bez obecnej elektrowni
        #     elektrownie.append(balans_mocy) # dodajemy balans_mocy do listy elektrownie

        return " ".join(map(str, elektrownie))

if __name__ == "__main__":
    n = int(input())
    moce_elektrowni = list(map(int, input().split())) # tworzymy liste z podstawowymi mocami elektrowni
    suma_mocy = sum(moce_elektrowni) # suma mocy w elektrowni

    zadanie = Praktyka_plus_teoria()
    print(zadanie.moceElektrowni(n, moce_elektrowni, suma_mocy))
    