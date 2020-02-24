from funkcionalnosti import *
from sort import *

if __name__ == '__main__':
    while True:
        directory = str(input("Unesite korenski direktorijum: "))
        if os.path.isdir(directory):
            break
        else:
            print("Putanja koju ste uneli nije direktorijum.Probajte ponovo\n")
            continue


    start_time = time.time()
    load(directory)
    print("1 -> Pretraga")
    print("2 -> Promenite broj rezultata po strani")
    print("6 -> Naredna strana")
    print("4 -> Prethodna strana")
    print("5 -> Ponovni prikaz opcija")
    print("0 -> Izlazak iz programa")
    print("-" * 140)
    start = 0
    end = 0
    n = 0
    broj_strana = 0
    vreme_pretrage = 0
    broj_rezultata_pretrage = 0
    print("Vreme ucitavanja: " + str(time.time() - start_time))
    
    while True:
        try:
            option = int(input("IZABERITE OPCIJU (za prikaz opcija pritisnite 5): "))
            if option not in (0, 1, 2, 4, 5, 6):
                raise Exception
        except:
            print("*****NEISPRAVNA OPCIJA*****")
            continue

        if option == 1:
            start = 0
            end = 0
            n = 0
            broj_strana = 0
            upit1 = str(input("Unesite upit: "))
            # Ovde ide kod za parsiranje pozivanje odgovarajuce funkcije za pretragu
            # Proba:
            start_time = time.time()
            list = []
            list.append(upit1)
            skup, dict1, i = traziSaOr(list)
            list = rangiraj(skup, dict1)
            merge_sort(list)
            broj_rezultata_pretrage = len(list)
            if skup.is_empty():
                print(" " * 15 + "*****NEMA REZULTATA PRETRAGE*****")
                continue

            print("***BROJ REZULTATA PRETRAGE: " + str(broj_rezultata_pretrage))
            vreme_pretrage = time.time() - start_time
            while True:
                try:
                    n = int(input("Unesite kol  iko rezultata po strani zelite da prikazete: "))
                    break
                except:
                    print("*****NEISPRAVAN UNOS*****")
                    continue

            while n > len(list) or n <= 0:
                try:
                    n = int(input("Nema toliko rezultata (ima ih " + str(
                    broj_rezultata_pretrage) + ") za prikaz ili ste uneli negativan broj, unesite ponovo n: "))
                except:
                    continue
            print("Vreme pretrage: " + str(vreme_pretrage))

            end = 1
            if len(list) % n == 0:
                broj_strana = len(list) / n
            else:
                broj_strana = len(list) // n + 1
            paginacija(list, start, end, n)
            print(" " * 15 + "STRANA " + str(start + 1) + " OD " + str(int(broj_strana)))
            print("-" * 140)

        elif option == 2:
            while True:
                try:
                    n = int(input("Unesite kol  iko rezultata po strani zelite da prikazete: "))
                    break
                except:
                    print("*****NEISPRAVAN UNOS*****")
                    continue
            while n > len(list) or n <= 0:
                print("Za odustanak pritisnite 0")
                try:
                    n = int(input("Nema toliko rezultata (ima ih " + str(
                    broj_rezultata_pretrage) + ") za prikaz ili ste uneli negativan broj, unesite ponovo n: "))
                except:
                    continue
                if n == 0:
                    break
            if n == 0:
                continue

            start = 0
            end = 1
            paginacija(list, start, end, n)
            if len(list) % n == 0:
                broj_strana = len(list) / n
            else:
                broj_strana = len(list) // n + 1
            print(" " * 15 + "STRANA " + str(start + 1) + " OD " + str(int(broj_strana)))
            print("-" * 140)
        elif option == 6:
            if start >= broj_strana - 1:
                print("NA POSLEDNJOJ STE STRANI")
                continue
            start += 1
            end += 1
            paginacija(list, start, end, n)
            print(" " * 15 + "STRANA " + str(start + 1) + " OD " + str(int(broj_strana)))
            print("-" * 140)

        elif option == 4:
            if start <= 0:
                print("NA PRVOJ STE STRANI")
                continue
            start -= 1
            end -= 1
            paginacija(list, start, end, n)
            print(" " * 15 + "STRANA " + str(start + 1) + " OD " + str(int(broj_strana)))
            print("-" * 140)
        elif option == 5:
            print("1 -> Pretraga")
            print("2 -> Promenite broj rezultata po strani")
            print("6 -> Naredna strana")
            print("4 -> Prethodna strana")
            print("5 -> Ponovni prikaz opcija")
            print("0 -> Izlazak iz programa")
            continue
        elif option == 0:
            break
