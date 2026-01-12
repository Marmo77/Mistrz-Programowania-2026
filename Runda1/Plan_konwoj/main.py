from collections import defaultdict, deque


class plan_konwoj:
    def __init__(self, polaczenia: list[tuple[int, int, int]]):
        self.polaczenia = polaczenia

    def uzupelnianie_grafu(self):
        graf: dict[int, list[tuple(int,int)]] = defaultdict(list) # -> wartosc domyslna [] dla list
        # tworzenie grafu - dla kazdego podanego muzeum a dodajemy (b, c) do grafu - b -> muzeum z polaczeniem, c -> poziom zagrozenia
        for a,b,c in self.polaczenia: # dla kazdego polaczenia utworz graf i dodaj tam jego wartosci
            graf[a].append((b,c))
            graf[b].append((a,c)) # dwukierunkowa, czyli w obie strony
        # print(graf)
        return graf
        # przykładowy wygląd grafu:
        # {
        #     1: [(2, 1), (5, 8)], 
        #     2: [(1, 1), (3, 3), (4, 2), (5, 1)], 
        #     3: [(2, 3), (4, 2), (5, 0)], 
        #     4: [(2, 2), (3, 2)], 
        #     5: [(1, 8), (2, 1), (3, 0)]
        # }

    def trasy_konwojow(self, q:int): # zwraca nam liste przejazdów konwojów
        trasy: list[tuple[int, int]] = []
        for _ in range(int(q)):
            odczytaj = input()
            x,y = map(int, odczytaj.split(' '))
            trasy.append((x,y))
            # x -> y - przejazdź z muzea o id x do muzea o id y
        return trasy


    def plan_konwoj(self, n: int, m: int) -> int:
        graf = self.uzupelnianie_grafu()
        # po uzupelnieniu grafu, pytamy o ilosc przejazdow i ich polaczenia
        q = input() # q -> liczba przejazdów
        trasy = self.trasy_konwojow(q)

        # print(graf)
        print("------------")
        # print(trasy)

        # teraz musimy sprawdzic czy da sie przejechac od muzeum x do muzeum y,
        # najproszym konwojem, z najmniejszym możliwmy zagrożeniem
        # ---- np. 
        # x = 1, y = 5
        # istnieje takie polaczenie 1->5, ale ma zagrozenie 8, sprawdzamy czy da sie dojsc do 5 z mniejszym zagrozeniem
        # 1->2->5 ma zagrozenie 1, 1, wiec da sie dojsc do 5 z zagrozeniem 1 
        for x, y in trasy: # x - muzeum startowe, y - muzeum docelowe
            for sasiad, zagrozenie in graf[x]: # sasiad - muzeum obok, zagrozenie - poziom zagrozenia na trasie do sasiada
                if sasiad == y: # jesli sasiad jest rowny y to znaczy ze da sie dojsc do y z zagrozeniem o poziomie 'zagrozenie'
                    print(f"Muzeum {x}, sasiad {sasiad}, zagrozenie {zagrozenie}") # wypisuje nam zagrozenie dla kazdej trasy naszego sasiada




    def da_sie_dojsc(self, graf, start, cel, max_zagrozenie):
        odwiedzone = set()
        kolejka = deque([start])
        odwiedzone.add(start)

        while kolejka:
            aktualny = kolejka.popleft()

            if aktualny == cel:
                return True
            
            for sasiad, zagrozenie in graf[aktualny]:
                if zagrozenie <= max_zagrozenie and sasiad not in odwiedzone:
                    odwiedzone.add(sasiad)
                    kolejka.append(sasiad)

        return False



if __name__ == "__main__":

    polaczenia: list[tuple[int, int, int]] = []

    # wczytywanie polaczen z inputa
    n,m = map(int, input().split()) # n - liczba muzeow, m - liczba konwojow
    for _ in range(m):
        a,b,c = map(int, input().split(' ')) # dzieli input na trzy czesci -> 1 2 3 i przypisuje do zmiennych
        # a -> b - połączenie miedzy muzeami o danych id, c -> poziom zagrożenia
        polaczenia.append((a,b,c))

    zadanie = plan_konwoj(polaczenia)
    zadanie.plan_konwoj(n, m)