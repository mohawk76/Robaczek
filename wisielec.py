def znajdzIndeksy(slowo, szukanyZnak): #szuka wszystkich indeksów dla wystąpienia znaku w słowie
    index = 0
    listaIndeksow = []

    for znak in slowo: #pętla wykonuje się dla każdego znaku w słowie
        if znak == szukanyZnak: #Sprawdzamy czy wybrany z słowa znak jest szukanym znakiem
            listaIndeksow.append(index) #Jeśli tak wrzucamy indeks znaku do listy
        index+=1
    
    return listaIndeksow

slowo = input("Wpisz słowo do zgadnięcia: ")

zgaduj = ""

for znak in slowo: #Tworzymy ciąg znaków które będzie przetrzymywać zgadnięte litery
    zgaduj += "_ "

iloscProb = 0

while True: #Nieskończona pętla
    print("Ilosc prob: " + str(iloscProb)) #Wyświetlamy ilość prób
    if iloscProb == 10: #Jeśli ilość prób jest równa 10, przegrałeś
        print("Nie zgadłeś! :P")
        print()
        break #Kończymy nieskończoną pętlę :o

    print(zgaduj) #wyświetlamy zgadnięte litery lub ich brak
    znak = input("Podaj litere lub całe słowo po znaku '@': ")

    if znak[0] == "@": #Jeśli pierwszy znak ciągu znaków to "@"
        if znak[1:] == slowo: #To sprawdzamy czy podane znaki po "@" to słowo do odgadnięcia
            zgaduj = slowo
            print(zgaduj)
            print("Brawo zgadłeś całe słowo! :P")
            print()
            break #Kończymy nieskończoną pętlę :o
        else:
            iloscProb +=1 #Zwiększa licznik prób
            
    elif znak in slowo: #Jeśli znak znajduje się w słowie
        indeksy = znajdzIndeksy(slowo, znak) #To pobierz wszystkie indeksy na których się znajduje
        for indeks in indeksy: #Dla każdego indeksu z listy
            temp = list(zgaduj) #przetwórz ciąg znaków na listę
            temp[indeks*2] = znak #Na przerobionym indeksie pod ciąg znaków z zgadniętymi literam zapisz zgadniętą litere 
            zgaduj = "".join(temp) #Przetwórz temp z powrotem na string i zapisz w zgaduj
    else:
            iloscProb +=1 #Zwiększa licznik prób
    
    if "".join(zgaduj.split()) == slowo: #jeśli zgaduj bez spacji jest równy slowo, wygrałes
        print(zgaduj)
        print("Brawo zgadłeś całe słowo! :P")
        print()
        break #Kończymy nieskończoną pętlę :o
        

input() #zatrzymuje wykonanie programu czekając na enter