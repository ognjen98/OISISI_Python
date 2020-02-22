from OISISI_Python.Python_projekat.funkcionalnosti import *

if __name__ == '__main__':
    directory = str(input("Unesite korenski direktorijum: "))
    load(directory)

    while True:
        print("1 -> Pretraga")
        print("2")
        print("0 -> Izlazak iz programa")
        option = int(input("IZABERITE OPCIJU"))

        if option == 1:
            upit = str(input("Unesite upit"))
            #Ovde ide kod za parsiranje pozivanje odgovarajuce funkcije za pretragu
            #Proga:
            start_time = time.time()
            skup, dict1 = trie.pronadjiRec(upit)
            print("Vreme pretrage: " + str(time.time() - start_time))
            list = ranking(skup, dict1)
            print("Broj rezultata pretrage: " + str(len(list)))
            for value in list:
                print(value)

        if option == 0:
            break