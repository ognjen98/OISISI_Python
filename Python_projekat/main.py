from funkcionalnosti import *
from sort import *
if __name__ == '__main__':
    directory = str(input("Unesite korenski direktorijum: "))
    start_time = time.time()
    load(directory)
    print("Vreme ucitavanja: " + str(time.time() - start_time))

    while True:
        print("1 -> Pretraga")
        print("2")
        print("0 -> Izlazak iz programa")
        try:
            option = int(input("IZABERITE OPCIJU"))
            if option not in (0, 1):
                raise Exception
        except:
            print("Nevalidna opcija")
            continue

        if option == 1:
            upit = str(input("Unesite upit"))
            #Ovde ide kod za parsiranje pozivanje odgovarajuce funkcije za pretragu
            #Proga:
            start_time = time.time()
            list = []
            list.append(upit)
            skup, dict1, i = traziSaOr(list)
            if i == 0:
                print("Nema rezultata pretrage")
            print("Vreme pretrage: " + str(time.time() - start_time))
            list = rangiraj(skup, dict1)
            merge_sort(list)
            print("Broj rezultata pretrage: " + str(len(list)))

            prikaz(list)


        elif option == 0:
            break
