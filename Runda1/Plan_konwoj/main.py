from collections import defaultdict, deque


class plan_konwoj:
    def plan_konwoj(self, n: int, m: int) -> int:
        polaczenia: list[tuple[int, int, int]] = []
        for _ in range(m):
            odczytaj = input()
            a,b,c = map(int, odczytaj.split(' ')) # dzieli input na trzy czesci -> 1 2 3 i przypisuje do zmiennych
            # a -> b - połączenie miedzy muzeami o danych id, c -> poziom zagrożenia
            polaczenia.append((a,b,c))

        print("-----------")
        # graf: dict[int, list[tuple[int, int]]] = {}
        graf: dict[int, list[tuple[int, int]]] = defaultdict(list)

        for a,b,c in polaczenia:
            # if a not in graf:
            #     graf[a] = []
            # if b not in graf:
            #     graf[b] = []
            graf[a].append((b,c))
            graf[b].append((a,c)) # dwukierunkowa, czyli w obie strony
        # print(graf.items())
        print(graf)

        
        # print(polaczenia)
        trasy: list[tuple[int,int]] = []
        q = int(input()) # q -> liczba przejazdów
        for _ in range(q):
            odczytaj = input()
            x,y = map(int, odczytaj.split(' '))
            trasy.append((x,y))
            # x -> y - przejazdź z muzea o id x do muzea o id y
        
        print("------------")

        for x,y in trasy:
            for z in range(0, n+1):
                if self.da_sie_dojsc(graf, x, y, z):
                    print(z)
                    break

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


# ZADANIE DO ANALIZY I DOWIEDZIEC SIE CO ROBI defaultdict I DEQUE 
        

            




if __name__ == "__main__":
    n,m = map(int, input().split()) # n - liczba muzeow, m - liczba konwojow

    zadanie = plan_konwoj()
    print(zadanie.plan_konwoj(n,m))