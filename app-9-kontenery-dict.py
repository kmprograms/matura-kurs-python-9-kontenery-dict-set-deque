from collections import Counter, defaultdict, deque

def slowniki_podstawy() -> None:
    # Słownik przechowuje pary klucz i wartość. Po kluczu szybko odczytuje się wartość,
    # bez przeszukiwania całej struktury. Klucze są unikalne i muszą być niemodyfikowalne:
    # liczby, napisy albo krotki. Wartości mogą być dowolne, także listy i inne słowniki.
    # Słownik pamięta kolejność dodawania par. Na maturze słownik służy głównie do dwóch
    # rzeczy: do zliczania wystąpień i do grupowania danych według wspólnej cechy.

    d1 = {"one": 1, "two": 2, "three": 3}
    d2 = dict(one=1, two=2, three=3)
    d3 = dict(zip(["one", "two", "three"], [1, 2, 3]))
    d4 = dict([("one", 1), ("two", 2), ("three", 3)])
    d5: dict[str, int] = {}
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
    print(d1 == d2 == d3 == d4)
    print(len(d1))  # len zwraca ile w dict jest par

    oceny = {"Jan": 4, "Ola": 5}
    print(oceny["Jan"])  # Wiemy jaka jest wartość pod kluczem "Jan", kiedy podasz klucz, którego nie ma
    # otrzymasz błąd KeyError
    print(oceny.get("Jan"))
    print(oceny.get("Ewa"))  # Brak klucza spowoduje, że get zwróci None
    print(oceny.get("Ewa", 0))  # Brak klucza spowoduje, że get zwróci wartość domyślną 0

    oceny["Ewa"] = 3
    oceny["Jan"] += 1
    print(oceny)

    del oceny["Ola"]  # usuwam parę o kluczu "Ola"
    print("Ola" in oceny)
    print("Jan" in oceny)
    print(oceny.pop("Ewa"))  # Usuwa parę, zwracając wartość
    print(oceny.pop("Ewa", -1))  # Jeśli klucza nie ma, zwróci wartość domyślną -1

    d6 = {"a": 10, "b": 20, "c": 30}
    print(d6.setdefault("b", 1000))  # Jest klucz, dlatego metoda zwraca wartość pod tym kluczem
    print(d6.setdefault("d", 9999))  # Nie ma klucza, dlatego wstawia do d6 parę z kluczem "d" i wartością 9999
    print(d6)

    d7 = {"a": 1, "b": 2}
    d8 = {"b": 3, "c": 4}
    print(d7 | d8)  # {'a': 1, 'b': 3, 'c': 4}
    print({**d7, **d8})


def przegladanie_slownika() -> None:
    pensje = {"adam": 2030, "ewa": 3222, "zosia": 3299}

    print("--- [ 1 ] ---")
    for imie in pensje:
        print(f"{imie=}, pensja = {pensje[imie]}")

    print("--- [ 2 ] ---")
    for imie, pensja in pensje.items():
        print(f"{imie=}, {pensja=}")

    print("--- [ 3 ] ---")
    print(list(pensje.keys()))
    print(list(pensje.values()))


def zliczanie_grupowanie() -> None:

    # Zliczanie
    imiona = ["adam", "ewa", "iza", "adam", "iza", "adam"]
    policzone: dict[str, int] = {}
    for imie in imiona:
        policzone[imie] = policzone.get(imie, 0) + 1
    print(policzone)

    # Grupowanie słów po liczbie znaków
    slowa = ["kot", "pies", "ul", "mysz", "lis", "osa"]
    grupy: dict[int, list[str]] = {}
    for slowo in slowa:
        slowo_dl = len(slowo)
        if slowo_dl not in grupy:
            grupy[slowo_dl] = []
        grupy[slowo_dl].append(slowo)
    print(grupy)


def klucz_z_najwieksza_wartoscia() -> None:
    liczniki = {"adam": 3, "ewa": 1, "iza": 2}

    najlepszy_klucz = max(liczniki, key=lambda k: liczniki[k])
    print("--- 1 ---")
    print(najlepszy_klucz)
    print(liczniki[najlepszy_klucz])

    najlepsze_imie, najlepszy_licznik = max(liczniki.items(), key=lambda pair: pair[1])
    print("--- 2 ---")
    print(najlepsze_imie)
    print(najlepszy_licznik)

    print("--- 3 ---")
    top = max(liczniki.values())
    print([k for k, v in liczniki.items() if v == top])  # wszystkie klucze z maksimum

    print("--- 4 ---")
    print(sorted(liczniki.items(), key=lambda pair: pair[1], reverse=True))


def wyrazenia_slownikowe() -> None:
    imiona = ["ala", "ola", "pawel", "zosia"]
    print({imie: len(imie) for imie in imiona if len(imie) > 3})

    d = {"a": 1, "b": 2, "c": 3}
    print({k: v for k, v in d.items() if v < 3})
    print({n: n ** 2 for n in range(1, 6)})


def typy_podobne_do_dict() -> None:

    # ---------------------------------------------------------------------------------------------------------
    # Counter
    # ---------------------------------------------------------------------------------------------------------
    imiona = ["adam", "ewa", "iza", "zosia", "adam", "iza", "adam"]
    cnt1 = Counter(imiona)
    print(cnt1)
    cnt2 = dict(cnt1)
    print(cnt2)
    print(cnt1["adam"])
    print(cnt1.most_common())
    print(cnt1.most_common(1))
    print(cnt1.most_common(2))
    imie, licznik = cnt1.most_common(1)[0]
    print(f"{imie=}, {licznik=}")

    litery = Counter("abrakadabra")
    print(litery)
    print(sorted(litery.elements()))
    print(list(litery.elements()))

    c1 = Counter(a=1, b=5, c=4)
    c2 = Counter(a=3, b=1, d=5)

    # c1["a"] += 3
    # print(c1)

    print(c1 + c2)
    print(c1 - c2)

    # ---------------------------------------------------------------------------------------------------------
    # defaultdict
    # ---------------------------------------------------------------------------------------------------------

    pary = [
        ("czerwony", 1),
        ("pomarańczowy", 3),
        ("czerwony", 2),
        ("niebieski", 4),
        ("pomarańczowy", 5),
        ("czerwony", 1)
    ]

    grupy1: defaultdict[str, list[int]] = defaultdict(list)
    for kolor, liczba in pary:
        grupy1[kolor].append(liczba)
    grupy2 = dict(grupy1)
    print(grupy1)
    print(grupy2)

    sumy: defaultdict[str, int] = defaultdict(int)
    for kolor, liczba in pary:
        sumy[kolor] += liczba
    print(dict(sumy))

    sumy_cnt = Counter()
    for kolor, liczba in pary:
        sumy_cnt[kolor] += liczba
    print(dict(sumy_cnt))


def zbiory() -> None:
    # Zbiór przechowuje elementy bez powtórzeń. Nie ma kolejności ani indeksów, więc nie działa odczyt
    # po indeksie ani wycinki. Sprawdzenie, czy element należy do zbioru, jest bardzo szybkie, niezależnie
    # od rozmiaru zbioru. Elementy zbioru muszą być niemodyfikowalne.
    s = {"zosia", "kamil", "adam", "iza", "adam", "iza"}
    print(s)
    print(len(s))
    print("adam" in s)

    imiona = ["adam", "ewa", "ewa", "adam", "ola"]
    print(sorted(set(imiona)))
    print(set("kmprograms"))

    s2 = {"adam", "ewa"}
    s2.add("zosia")
    s2.add("adam")
    s2.remove("ewa")  # KeyError, kiedy nie ma elementu
    s2.discard("ewa")  # bez błędu, kiedy nie ma elementu
    print(sorted(s2))

    # Wyrażenie zbiorowe
    cyfry_jednosci = {n % 10 for n in [12, 22, 35, 41, 52]}
    print(cyfry_jednosci)

    s3 = set()

    # Działania na zbiorach
    a = {11, 22, 33}
    b = {22, 33, 44}
    print("Działania na zbiorach")
    print(sorted(a | b))
    print(sorted(a & b))
    print(sorted(a - b))
    print(sorted(a ^ b))
    print({22} <= a)
    print({22, 33} < a)
    print(a == {33, 22, 11})
    print(a.isdisjoint({1, 2}))  # czy zbiory nie mają wspólnych elementów


def kolejki() -> None:
    # deque z modułu collections pozwala szybko dodawać i usuwać elementy z obu końców.
    # Lista robi to szybko tylko na końcu. Operacje pop z zerem i insert z zerem na liście
    # przesuwają wszystkie pozostałe elementy. Dla dużych list są wolne.
    d = deque([1, 2, 3])
    d.append(4)  # na koniec
    d.appendleft(0)  # na początek
    print(d)
    print(d.pop())  # z końca
    print(d.popleft())  # z początku
    print(d)
    d.rotate(1)  # przesunięcie w prawo: ostatni idzie na początek
    print(d)
    d.rotate(-1)
    print(d)

    ostatnie_trzy: deque[int] = deque(maxlen=3)
    for x in [5, 6, 7, 8]:
        ostatnie_trzy.append(x)
    print(ostatnie_trzy)
    print(list(ostatnie_trzy))

def main() -> None:
    # slowniki_podstawy()
    # przegladanie_slownika()
    # zliczanie_grupowanie()
    # klucz_z_najwieksza_wartoscia()
    # wyrazenia_slownikowe()
    typy_podobne_do_dict()
    # zbiory()
    # kolejki()

    """
    Używaj listy, gdy dane trzeba przetwarzać po kolei, dopisywać, usuwać lub sortować. To 
    domyślny wybór przy wczytywaniu kolejnych wierszy z pliku.
    
    Używaj krotki, gdy kilka wartości tworzy jeden niezmienny rekord, na przykład para współrzędnych. 
    Krotka przydaje się też wtedy, gdy funkcja zwraca kilka wyników albo gdy potrzebujesz złożonego 
    klucza słownika.
    
    Używaj namedtuple, gdy rekord ma kilka pól i chcesz odwoływać się do nich po nazwie, a nie po indeksie. 
    Kod staje się czytelniejszy, na przykład wiersz.wynik zamiast wiersz[2].
    
    Używaj słownika, gdy wartość trzeba szybko odczytać po kluczu, na przykład wynik po nazwisku. Sprawdza 
    się też przy zliczaniu i grupowaniu danych.
    
    Używaj Countera, gdy trzeba policzyć, ile razy występuje każdy element. Metoda most_common() od razu zwraca 
    elementy najczęstsze.
    
    Używaj defaultdict, gdy grupujesz lub sumujesz dane po kluczu i nie chcesz za każdym razem sprawdzać, czy 
    klucz już istnieje. Przy brakującym kluczu sam tworzy wartość domyślną, na przykład pustą listę lub zero.
    
    Używaj zbioru, gdy liczą się tylko unikalne elementy albo gdy wiele razy sprawdzasz, czy element występuje 
    w danych. Przydaje się też do działań na zbiorach, takich jak część wspólna i różnica.
    
    Używaj deque, gdy dodajesz lub usuwasz elementy na obu końcach, czyli przy kolejce lub stosie. Metoda rotate() 
    wykonuje przesunięcie cykliczne.
    """


if __name__ == '__main__':
    main()