class NoworoczneZyczenia:
    

    # def czy_jest_liczba_szczesliwa(self, liczba: int):

        # szcz_liczba = str(liczba)
        
        # while len(szcz_liczba) > 1:
        #     suma = 0
        #     for i in szcz_liczba:
        #         suma += int(i)
            
        #     if len(str(suma)) == 1:
        #         szcz_liczba = suma
        #         break
        #     else:
        #         szcz_liczba = str(suma)
        
        # if szcz_liczba == 1:
        #     return "Szczesliwego Nowego Roku"
        # else:
        #     return szcz_liczba

    # 75 / 100, konwesja na int zabiera za duzo miejsca

    def czy_jest_liczba_szczesliwa(self, szcz_liczba: str):
        
        while len(szcz_liczba) > 1:
            suma = 0
            for i in szcz_liczba:
                suma += int(i)
            
            szcz_liczba = str(suma)
        
        szcz_liczba = int(szcz_liczba)
        if szcz_liczba == 1:
            return "Szczesliwego Nowego Roku"
        else:
            return szcz_liczba
        


if __name__ == "__main__":
    
    # liczba = int(input())
    liczba = input()

    noworoczne_zyczenia = NoworoczneZyczenia()
    print(noworoczne_zyczenia.czy_jest_liczba_szczesliwa(liczba))