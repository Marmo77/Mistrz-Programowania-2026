#ciecia - int dodatnie >= 10

# ciecia liczby 14379 to:

#-------------
# 1 i 4379
# 14 i 379
# 143 i 79
# 1437 i 9
#-------------

# k: int = 0

def ciecie_na_polowie(k :int):
    #k: int, >= 10,
    # 2 połowy będą równe więc
    dlugosc = 0
    kopia_liczby = k
    while kopia_liczby > 0:
        dlugosc = dlugosc + 1
        kopia_liczby = kopia_liczby // 10 # skracamy od tyłu czyli np 1200 -> 120 -> 12 -> 1 -> 0



    polowa_dlugosci = dlugosc // 2 # polowa czyli z 6 = 3
    dzielnik = 1
    licznik = 0 #pomocnicza aby wyjsc z while'a

    #dzielnik = 10**{połowa długości czyli jeśli 123456 to długość = 6 to jest 6/2 = 3} => 10**3 => 1000

    while licznik < polowa_dlugosci:
        dzielnik = dzielnik * 10
        licznik = licznik + 1
    #to da nam wynik dzielnika jako połowa zamiast pisać 10**polowa_dlugosci to to zrobiliśmy, ale bez uzycia funkcji pythona
    #obliczanie a
    a = k // dzielnik # początkowe wyrazy
    b = k % dzielnik # ostatnie wyrazy od płowy

    #---------------------
    #obliczanie b - skąplikowane
    # b = 0
    # # mnoznik =  10**(pierwsza_p_dlugosci-1)# mnoznik jest od polowy czyli jesli mamy 456 czyli 3 liczby to zaczynamy od * 100 poznie * 10 i * 1
    # mnoznik_b = 1
    # ponad_polowa = 10**pierwsza_p_dlugosci
    # for i in range(dlugosc): # powtarza sie tyle ile ma dlugosc, ale robi coś dopiero w momencie gdy jest od polowy
    #
    #     aktualna = k // 10**i
    #     if ponad_polowa < aktualna: # gdy aktualna jest wieksza od polowy czyli 1234 > 1000 bo polowa to 3 to od tego momentu czyli 4,5,6 przy 123456
    #         ostatnia_l = aktualna % 10 # bierze reszte (czyli ostatnią liczbę z dzielenia
    #         b = b + ostatnia_l * mnoznik_b
    #         mnoznik_b = mnoznik_b * 10

    # print(b)
    print(f"a: {a} i b: {b}")

ciecie_na_polowie(123456)