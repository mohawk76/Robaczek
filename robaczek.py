import random
import os

# DONE Stworzyć klasę Obiekt
# Klasa Obiekt ma atrybuty x i y , które są współrzędnymi obiektu

class Obiekt(object):
    def __init__(self, x, y):  # konstruktor klasy Obiekt przyjmujcy parametry x i y
        self._x = x  # ustawienie atrybutu protected x na wartość podaną w argumencie x
        self._y = y  # ustawienie atrybutu protected y na wartość podaną w argumencie y
    
    def pobierzPozycje(self): #Zwraca współrzędne x i y obiektu
        return [self._x, self._y]

# DONE Stworzyć klasę Robaczek
# Klasa Robaczek ma posiadać atrybuty zawierające: prędkość, poziom i najedzenie
# Ma posiadać metody zjedzOwoc przyjmuje obiekt typu Owoc(dodanie wartości z owocu do parametru najedzenie i usunięcie elementu z listy) oraz metodę sprawdź poziom, która ustawia poziom Robaczka jeżeli zje odpowiednią ilość owoców


class Robaczek(Obiekt):  # klasa Robaczek dziedziczy po klasie Obiekt
    def __init__(self, x, y):  # konstruktor przyjmuje parametry x i y i tworzy nowy obiekt robaczek
        # wywołujemy konstruktor klasy Obiekt by zainicjować atrybuty _x i _y
        super().__init__(x, y)
        self._predkosc = 1  # ustawiamy prędkość robaczka na 1
        self._poziom = 0  # ustawiamy poziom robaczka na 0
        self._najedzenie = 0  # ustawiamy najedzenie robaczka na 0

    def zjedzOwoc(self, owoc):  # metoda zjedzOwoc przyjmuje parametr typu Owoc
        # pobieramy wartość jedzenia owocu i dodajemy do najedzenia robaczka
        self._najedzenie += owoc.pobierzJedzenie()
        Owoc.listaOwockow.remove(owoc)  # usuwamy zjedzony owoc z listy

    # metoda zwiększa poziom robaczka o wielokrotność 3, po każdym wykonaniu
    def sprawdzPoziom(self):
        self._poziom = int(self._najedzenie / 3)

    def pobierzPoziom(self): #metoda zwraca wartość poziomu
        return self._poziom

    def ruch(self, kierunek): #odpowiada za poruszenie się robaczka w jednym z czterech kierunków

        #Wskazówka: w naszym układzie współrzędnych, współrzędne [0,0] oznaczają lewy górny róg konsoli

        if kierunek == 'w': #ruch w góre
            self._y -= 1
        elif kierunek == 's': #ruch w dół
            self._y += 1
        elif kierunek == 'a': #ruch w lewo
            self._x -= 1
        elif kierunek == 'd': #ruch w prawo
            self._x += 1
        
        #Normalizacja x by robaczek nie znalazł się po za planszą
        if(self._x < 0):
            self._x = 0
        elif(self._x > 9):
            self._x = 9
        
        #Normalizacja y by robaczek nie znalazł się po za planszą
        if(self._y < 0):
            self._y = 0
        elif(self._y > 9):
            self._y = 9

# DONE Stworzyć klasę Owoc
# Klasa Owoc posiada atrybut jedzenie o losowej wartości z przedziału 1-5

class Owoc(Obiekt):
    listaOwockow = [] #Atrybut klasy Owoc, będący listą obiektów typu Owoc(przykład odwołania: Owoc.listaOwockow[0])

    def __init__(self, x, y): #Konstruktor klasy Owoc tworzący nowy obiekt typu Owoc, przyjmuje parametry x i y
        super().__init__(x,y) #Wywołanie konstruktora klasy bazowej Obiekt i zainicjowanie atrybutów obiektu _x i _y
        self._jedzenie = random.randint(1,5) #Inicjacja atrybutu _jedzenie wartością losową z zakresu 1-5
    
    def pobierzJedzenie(self): #Metoda zwraca wartość atrybutu _jedzenie
        return self._jedzenie


# DONE Stworzyć funkcję sprawdzKolizje
# Przyjmuje 2 argumenty: typu Robaczek oraz Owoc i ma sprawdzać czy znajdują się na tym samym polu

def sprawdzKolizje(robaczek, owoc): #Funkcja sprawdza kolizje 2 obiektów, przyjmuje argument robaczek typu Robaczek i owoc typu Owoc
    if robaczek.pobierzPozycje() == owoc.pobierzPozycje(): #Jeśli pozycja obiektów jest taka sama zwraca True
        return True
    else: #Jeśli pozycja jest inna zwraca False
        return False

# DONE Stworzyć funkcję wczytajDane
# Dane na start wczytujemy z pliku Data.txt(współrzędne obiektów)

def wczytajDane(sciezkaPliku): #Funkcja wczytuje dane z pliku do którego ścieżka jest zapisana w parametrze sciezkaPliku
    file = open(sciezkaPliku, "r") #Otwieramy plik z prawami do odczytu

    buffer = file.readline() #Czytamy pierwszą linię która odpowiada za współrzędne robaczka 
    x,y = buffer.split() #Dzielimy wczytaną linię na 2 i zapisujemy w zmeinnych x i y
    robaczek = Robaczek(int(x), int(y)) #Tworzymy obiekt robaczek z wczytanymi współrzędnymi

    buffer = file.readline() #Czytamy drugą linię

    while not(buffer == ''): #Wczytujemy współrzędne z pliku dopóki nie natrafimy na pusty łańcuch znaków
        x,y = buffer.split() #Dzielimy kolejną linie i wynik zapisujemy w zmiennych x i y
        Owoc.listaOwockow.append(Owoc(int(x), int(y))) #Tworzymy obiekt owoc z wczytanymi współrzędnymi i zapisujemy w liście owoców
        buffer = file.readline() #Czytamy kolejną linię
    
    file.close() #zamykamy plik
    return robaczek #Zwracamy utworzony obiekt klasy Robaczek


# DONE Stworzyć funkcję pobierzWejscie
# Użytkownik wpisuje na klawiaturze gdzie ma poruszać się robaczek

def pobierzWejscie():
    wejscie = input("Podaj kierunek w którym chcesz się poruszyć: ") #pobieramy dane od gracza

    if wejscie in ['w','s','a','d']: #sprawdzamy czy gracz podał poprawny kierunek ruchu. Jeśli tak zwracamy wpisany kierunek, jeśli nie nic nie robimy
        return wejscie

# DONE Stworzyć funkcję rysujPlansze
# Rysuje planszę, robaczka i owoce

def rysujPlansze(robaczek): #Funkcja rysuje plansze i obiekty znajdujące się na niej
    wysokosc = 10
    szerokosc = 10

    plansza = ""

    plansza += "Poziom: " + str(robaczek.pobierzPoziom()) + "\n" #Rysujemy napis z wartością poziomu robaczka

    #Rysujemy sufit planszy
    plansza += "+"
    for i in range(szerokosc-1):
        plansza += "--"
    plansza += "-+\n"

    #Rysujemy środek naszej planszy i ścianki boczne
    for y in range(1,wysokosc):
        plansza += "| "
        for x in range(1,szerokosc):
            if robaczek.pobierzPozycje() == [x,y]: #Sprawdzamy czy robaczek znajduje się na tych współrzędnych
                plansza += "O "
            elif Owoc.listaOwockow[0].pobierzPozycje() == [x,y]: #Sprawdzamy czy pierwszy owoc na liście znajduje się na tych wspórzędnych
                plansza += "* "
            else: #Jeśli nic nie znajduje się na tych współrzędnych rysuje puste miejsce
                plansza += "  "
        plansza += "|\n"

    #Rysujemy podłogę planszy
    plansza += "+"
    for i in range(szerokosc-1):
        plansza += "--"
    plansza += "-+\n"
    
    os.system("cls") #czyścimy konsole
    print(plansza) #Wyświetlamy naszą piękną planszę

# DONE Stworzyć funkcję Gra
# Zawiera główną pętlę gry, która kończy swoje działanie gdy robaczek zje wszystkie owoce(lista owoców będzie pusta)

def Gra(): #Główna funkcja gry
    robaczek = wczytajDane("Data.txt") #wczytujemy dane i zapisujemy zwrócony przez funkcje obiekt robaczka

    while not(len(Owoc.listaOwockow) == 0): #wykonujemy pętle dopóki w liście znajdują się owoce
        rysujPlansze(robaczek) #rysukemy plansze z przekazanym robaczkiem
        kierunek = pobierzWejscie() #pobieramy od użytkownika kierunek
        robaczek.ruch(kierunek) #poruszamy robaczkiem w danym kierunku
        if sprawdzKolizje(robaczek, Owoc.listaOwockow[0]): #sprawdzamy czy doszło do kolizji
            robaczek.zjedzOwoc(Owoc.listaOwockow[0]) #jeśli doszło do kolizji zjdamy pierwszy owoc na liście
            robaczek.sprawdzPoziom() #po czym aktualizujemy aktualny poziom robaczka

Gra() # wywołujemy główną funkcję gry