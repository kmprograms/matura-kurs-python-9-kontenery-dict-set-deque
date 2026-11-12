**Polski** · [English](README.en.md)

---

# Matura - informatyka, poziom rozszerzony, kurs Pythona, część 9. "Kontenery: dict, set, deque"

> ### 🎬 Wideo z omówieniem
> Pełne omówienie tego materiału krok po kroku znajdziesz na moim kanale YouTube:
> **[Link do filmu na YouTube](https://youtu.be/zeLSmTVsogI)**
>
> Na filmie tworzę słowniki na kilka sposobów i pokazuję zliczanie oraz grupowanie danych. Omawiam też typy `Counter` i `defaultdict` z modułu `collections`, zbiory `set` oraz kolejkę `deque`. Na koniec podsumowuję, kiedy używać którego kontenera.

---

## Spis treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Uruchomienie](#uruchomienie)
- [Struktura projektu](#struktura-projektu)
- [Omówione zagadnienia](#omówione-zagadnienia)
- [Zgodność z zasadami egzaminu](#zgodność-z-zasadami-egzaminu)
- [Kiedy używać którego kontenera](#kiedy-używać-którego-kontenera)
- [Wyniki](#wyniki)
- [Uwagi implementacyjne](#uwagi-implementacyjne)

## Opis

Kod do 9. części kursu Pythona, w którym przygotowuję do matury z informatyki na poziomie rozszerzonym. Ta część zamyka temat kontenerów. Po listach i krotkach przyszła kolej na słownik `dict`, jego specjalne odmiany `Counter` i `defaultdict`, zbiór `set` i kolejkę `deque`.

Słownik przechowuje pary klucz i wartość. Po kluczu szybko odczytuje się wartość, bez przeszukiwania całej struktury. W liście, gdy nie znasz pozycji szukanego elementu, trzeba przeglądać elementy jeden po drugim. W słowniku po prostu pytasz, czy istnieje dany klucz.

Na maturze słownik służy głównie do dwóch rzeczy: do zliczania wystąpień i do grupowania danych według wspólnej cechy. Dlatego obie operacje pokazuję najpierw na zwykłym słowniku, a potem z użyciem `Counter` i `defaultdict`, które je upraszczają.

Cały nowy kod z tego nagrania znajduje się w pliku `app-9-kontenery-dict.py`. Pozostałe pliki pochodzą z wcześniejszych części kursu. W kolejnym nagraniu omawiam napisy.

## Wymagania

- Python 3.10 lub nowszy. Plik `app-4-instrukcje-warunkowe.py` korzysta z instrukcji `match`, dostępnej od Pythona 3.10. Plik `app-9-kontenery-dict.py` używa operatora `|` do łączenia słowników oraz adnotacji typu `dict[str, int]`, które działają od Pythona 3.9.
- Brak zewnętrznych zależności. Wykorzystano wyłącznie bibliotekę standardową, czyli moduły `collections`, `random` i `math`.

## Uruchomienie

```bash
git clone https://github.com/kmprograms/matura-kurs-python-9-kontenery-dict-set-deque
cd matura-kurs-python-9-kontenery-dict-set-deque
python app-9-kontenery-dict.py
```

Każdy temat z nagrania jest zamknięty w osobnej funkcji. Funkcja `main` wywołuje w danej chwili tylko jedną z nich, a pozostałe wywołania są zakomentowane:

```python
def main() -> None:
    # slowniki_podstawy()
    # przegladanie_slownika()
    # zliczanie_grupowanie()
    # klucz_z_najwieksza_wartoscia()
    # wyrazenia_slownikowe()
    typy_podobne_do_dict()
    # zbiory()
    # kolejki()
```

Żeby uruchomić inny przykład, odkomentuj wybrane wywołanie w `main`. Pliki z wcześniejszych części kursu uruchamiasz tak samo, na przykład `python app-8-kontenery-tuple.py`.

## Struktura projektu

| Plik | Opis |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | Pierwszy program, zmienne, f-stringi, operatory arytmetyczne i zamiana typów |
| `app-2-liczby-calkowite.py` | Działania na liczbach całkowitych, operatory `//` i `%`, operatory relacji, spójniki logiczne, cyfry liczby |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Wczytywanie danych przez `input` (w komentarzu), moduł `random`, systemy liczbowe, operacje bitowe, moduł `math` |
| `app-4-instrukcje-warunkowe.py` | Instrukcje `if`, `elif`, `else`, wyrażenie warunkowe, instrukcja `match`, funkcje `min`, `max` i `abs` |
| `app-5-petle.py` | Pętle `while` i `for`, `range`, `break`, `continue`, pętla w pętli |
| `app-6-funkcje.py` | Funkcje, parametry, argumenty domyślne i nazwane, `return`, zwracanie kilku wartości, funkcja `main` |
| `app-7-kontenery-listy.py` | Listy, metody list, wycinki, listy dwuwymiarowe, wyrażenia listowe i wyrażenia generatora |
| `app-8-kontenery-tuple.py` | Krotki i `namedtuple` |
| `app-9-kontenery-dict.py` | Kod z tego nagrania: słowniki, `Counter`, `defaultdict`, zbiory i `deque` |

## Omówione zagadnienia

### Tworzenie słownika i podstawowe operacje

Funkcja `slowniki_podstawy`. Słownik można utworzyć na kilka sposobów: z nawiasów klamrowych, z argumentów nazwanych funkcji `dict`, z dwóch list połączonych przez `zip` albo z listy krotek. Wszystkie cztery sposoby dają ten sam słownik, co potwierdza porównanie `d1 == d2 == d3 == d4`.

```python
d1 = {"one": 1, "two": 2, "three": 3}
d2 = dict(one=1, two=2, three=3)
d3 = dict(zip(["one", "two", "three"], [1, 2, 3]))
d4 = dict([("one", 1), ("two", 2), ("three", 3)])
d5: dict[str, int] = {}
```

Klucze są unikalne i muszą być niemodyfikowalne, na przykład liczby, napisy albo krotki. Wartości mogą być dowolne, także listy i inne słowniki. Funkcja `len` zwraca liczbę par w słowniku.

Odczyt wartości:

- `oceny["Jan"]` zwraca wartość pod kluczem, a dla brakującego klucza zgłasza błąd `KeyError`
- `oceny.get("Ewa")` dla brakującego klucza zwraca `None`
- `oceny.get("Ewa", 0)` dla brakującego klucza zwraca wartość domyślną `0`

Słownik jest modyfikowalny, tak jak lista. Przypisanie `oceny["Ewa"] = 3` dodaje nową parę, a `oceny["Jan"] += 1` zmienia istniejącą wartość. `del` usuwa parę, a `in` sprawdza, czy klucz istnieje. `pop` usuwa parę i zwraca jej wartość, a z drugim argumentem zwraca wartość domyślną, gdy klucza nie ma. `setdefault` zwraca wartość pod istniejącym kluczem albo wstawia nową parę, gdy klucza brakuje.

Łączenie słowników:

```python
d7 = {"a": 1, "b": 2}
d8 = {"b": 3, "c": 4}
print(d7 | d8)  # {'a': 1, 'b': 3, 'c': 4}
print({**d7, **d8})
```

W obu zapisach przy powtarzającym się kluczu wygrywa wartość ze słownika po prawej stronie, a nowe klucze z prawego słownika trafiają na koniec wyniku.

### Przeglądanie słownika

Funkcja `przegladanie_slownika`. Pętla `for` po słowniku daje kolejne klucze. Widok `items()` daje pary, które od razu rozpakowujesz do dwóch zmiennych:

```python
for imie, pensja in pensje.items():
    print(f"{imie=}, {pensja=}")
```

Widoki `keys()` i `values()` zwracają same klucze albo same wartości. Funkcja `list` zamienia je na zwykłą listę.

### Zliczanie i grupowanie na zwykłym słowniku

Funkcja `zliczanie_grupowanie`. Zliczanie wystąpień imion z użyciem `get` z wartością domyślną `0`:

```python
for imie in imiona:
    policzone[imie] = policzone.get(imie, 0) + 1
```

Wynik: `{'adam': 3, 'ewa': 1, 'iza': 2}`.

Grupowanie słów według liczby znaków. Gdy klucza jeszcze nie ma, trzeba najpierw utworzyć pod nim pustą listę:

```python
for slowo in slowa:
    slowo_dl = len(slowo)
    if slowo_dl not in grupy:
        grupy[slowo_dl] = []
    grupy[slowo_dl].append(slowo)
```

Wynik: `{3: ['kot', 'lis', 'osa'], 4: ['pies', 'mysz'], 2: ['ul']}`.

### Klucz z największą wartością i sortowanie

Funkcja `klucz_z_najwieksza_wartoscia`. Pokazuję trzy podejścia do szukania maksimum w słowniku `{"adam": 3, "ewa": 1, "iza": 2}`:

1. `max(liczniki, key=lambda k: liczniki[k])` zwraca klucz z największą wartością
2. `max(liczniki.items(), key=lambda pair: pair[1])` zwraca całą parę, którą rozpakowujesz do dwóch zmiennych
3. `max(liczniki.values())` wyznacza największą wartość, a wyrażenie listowe zbiera wszystkie klucze, które ją mają

Sortowanie par według wartości, malejąco:

```python
print(sorted(liczniki.items(), key=lambda pair: pair[1], reverse=True))
```

Wynik: `[('adam', 3), ('iza', 2), ('ewa', 1)]`. Funkcji `min` używasz w ten sam sposób co `max`.

### Wyrażenia słownikowe

Funkcja `wyrazenia_slownikowe`. Tak jak wyrażenie listowe tworzy nową listę, wyrażenie słownikowe tworzy nowy słownik. Źródłem danych może być lista, inny słownik albo `range`:

```python
imiona = ["ala", "ola", "pawel", "zosia"]
print({imie: len(imie) for imie in imiona if len(imie) > 3})

d = {"a": 1, "b": 2, "c": 3}
print({k: v for k, v in d.items() if v < 3})
print({n: n ** 2 for n in range(1, 6)})
```

Wyniki kolejno: `{'pawel': 5, 'zosia': 5}`, `{'a': 1, 'b': 2}` oraz `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`.

### Counter i defaultdict

Funkcja `typy_podobne_do_dict`. Oba typy pochodzą z modułu `collections` i upraszczają zliczanie oraz grupowanie.

`Counter` zlicza wystąpienia elementów listy albo znaków napisu w jednym wywołaniu. `dict(cnt1)` zamienia wynik na zwykły słownik. Metoda `most_common()` zwraca pary uporządkowane malejąco według liczby wystąpień, a `most_common(n)` tylko `n` najczęstszych:

```python
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
```

Metoda `elements()` zwraca każdy element tyle razy, ile wynosi jego licznik. Obiekty `Counter` można też dodawać i odejmować:

```python
c1 = Counter(a=1, b=5, c=4)
c2 = Counter(a=3, b=1, d=5)

# c1["a"] += 3
# print(c1)

print(c1 + c2)
print(c1 - c2)
```

Przy dodawaniu liczniki tych samych kluczy się sumują. Przy odejmowaniu w wyniku zostają tylko klucze z dodatnią liczbą wystąpień.

`defaultdict` sam tworzy wartość domyślną dla brakującego klucza. `defaultdict(list)` tworzy pustą listę, a `defaultdict(int)` wartość `0`. Dzięki temu grupowanie nie wymaga już sprawdzania klucza instrukcją `if`:

```python
grupy1: defaultdict[str, list[int]] = defaultdict(list)
for kolor, liczba in pary:
    grupy1[kolor].append(liczba)
```

Sumowanie wartości po kluczu zapiszesz przez `defaultdict(int)` albo przez `Counter`, z tym samym wynikiem. `Counter` ma dodatkowo metody takie jak `most_common`.

```python
sumy: defaultdict[str, int] = defaultdict(int)
for kolor, liczba in pary:
    sumy[kolor] += liczba
print(dict(sumy))
```

### Zbiory set

Funkcja `zbiory`. Zbiór przechowuje elementy bez powtórzeń. Nie ma kolejności ani indeksów, więc nie działa odczyt po indeksie ani wycinki. Sprawdzenie, czy element należy do zbioru, jest bardzo szybkie, niezależnie od rozmiaru zbioru. Elementy zbioru muszą być niemodyfikowalne.

W kodzie pokazuję:

- usuwanie duplikatów z listy przez `set(imiona)` i z napisu przez `set("kmprograms")`
- metody `add`, `remove` (błąd `KeyError`, gdy elementu nie ma) oraz `discard` (bez błędu)
- wyrażenie zbiorowe `{n % 10 for n in [12, 22, 35, 41, 52]}`
- tworzenie pustego zbioru przez `set()`, bo `{}` tworzy pusty słownik
- działania na zbiorach

```python
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
```

Znaczenie operatorów i wyniki:

- `a | b` - suma zbiorów: `[11, 22, 33, 44]`
- `a & b` - część wspólna: `[22, 33]`
- `a - b` - różnica, w której ma znaczenie kolejność zbiorów: `[11]`
- `a ^ b` - różnica symetryczna, czyli elementy obecne tylko w jednym ze zbiorów: `[11, 44]`
- `{22} <= a`, `{22, 33} < a` oraz `a == {33, 22, 11}` - porównania zbiorów, wszystkie dają `True`, bo w zbiorach kolejność nie ma znaczenia
- `a.isdisjoint({1, 2})` - sprawdza, czy zbiory nie mają wspólnych elementów: `True`

### Kolejka deque

Funkcja `kolejki`. `deque` z modułu `collections` pozwala szybko dodawać i usuwać elementy z obu końców. Lista robi to szybko tylko na końcu. Operacje `pop` z zerem i `insert` z zerem na liście przesuwają wszystkie pozostałe elementy, więc dla dużych list są wolne.

```python
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
```

Wynik:

```
deque([0, 1, 2, 3, 4])
4
0
deque([1, 2, 3])
deque([3, 1, 2])
deque([1, 2, 3])
```

Kolejka z parametrem `maxlen=3` przechowuje najwyżej trzy elementy. Po dodaniu liczb `5, 6, 7, 8` zostają `6, 7, 8`, a piątka wypada. Na koniec `list(ostatnie_trzy)` zamienia kolejkę na zwykłą listę. W dalszej części kursu, przy algorytmach, pokażę, jak za pomocą `deque` zrobić stos.

## Zgodność z zasadami egzaminu

Na maturze wszędzie tam, gdzie treść zadania nie zabrania czegoś wprost, możesz korzystać ze wszystkiego, co daje biblioteka standardowa Pythona. `Counter`, `defaultdict` i `deque` pochodzą z modułu `collections`, który jest jej częścią. Możesz więc ich używać na przykład przy zliczaniu danych wczytanych z pliku. Jeżeli wolisz zostać przy zwykłym słowniku, zliczanie i grupowanie zapiszesz tak jak w funkcji `zliczanie_grupowanie`.

## Kiedy używać którego kontenera

Podsumowanie z końca nagrania zapisałem w docstringu w funkcji `main`:

| Kontener | Kiedy używać |
| --- | --- |
| `list` | Gdy dane trzeba przetwarzać po kolei, dopisywać, usuwać lub sortować. To domyślny wybór przy wczytywaniu kolejnych wierszy z pliku. |
| `tuple` | Gdy kilka wartości tworzy jeden niezmienny rekord, na przykład para współrzędnych. Krotka przydaje się też wtedy, gdy funkcja zwraca kilka wyników albo gdy potrzebujesz złożonego klucza słownika. Krotka jest niemodyfikowalna, a klucze słownika też muszą takie być. |
| `namedtuple` | Gdy rekord ma kilka pól i chcesz odwoływać się do nich po nazwie, a nie po indeksie. Kod staje się czytelniejszy, na przykład `wiersz.wynik` zamiast `wiersz[2]`. |
| `dict` | Gdy wartość trzeba szybko odczytać po kluczu, na przykład wynik po nazwisku. Sprawdza się też przy zliczaniu i grupowaniu danych. |
| `Counter` | Gdy trzeba policzyć, ile razy występuje każdy element. Metoda `most_common()` od razu zwraca elementy najczęstsze. |
| `defaultdict` | Gdy grupujesz lub sumujesz dane po kluczu i nie chcesz za każdym razem sprawdzać, czy klucz już istnieje. Przy brakującym kluczu sam tworzy wartość domyślną, na przykład pustą listę lub zero. |
| `set` | Gdy liczą się tylko unikalne elementy albo gdy wiele razy sprawdzasz, czy element występuje w danych. Przydaje się też do działań na zbiorach, takich jak część wspólna i różnica. |
| `deque` | Gdy dodajesz lub usuwasz elementy na obu końcach, czyli przy kolejce lub stosie. Metoda `rotate()` wykonuje przesunięcie cykliczne. |

## Wyniki

W obecnej wersji pliku funkcja `main` wywołuje `typy_podobne_do_dict`. Po uruchomieniu `python app-9-kontenery-dict.py` program wypisuje:

```
Counter({'adam': 3, 'iza': 2, 'ewa': 1, 'zosia': 1})
{'adam': 3, 'ewa': 1, 'iza': 2, 'zosia': 1}
3
[('adam', 3), ('iza', 2), ('ewa', 1), ('zosia', 1)]
[('adam', 3)]
[('adam', 3), ('iza', 2)]
imie='adam', licznik=3
Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
['a', 'a', 'a', 'a', 'a', 'b', 'b', 'd', 'k', 'r', 'r']
['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'k', 'd']
Counter({'b': 6, 'd': 5, 'a': 4, 'c': 4})
Counter({'b': 4, 'c': 4})
defaultdict(<class 'list'>, {'czerwony': [1, 2, 1], 'pomarańczowy': [3, 5], 'niebieski': [4]})
{'czerwony': [1, 2, 1], 'pomarańczowy': [3, 5], 'niebieski': [4]}
{'czerwony': 4, 'pomarańczowy': 8, 'niebieski': 4}
{'czerwony': 4, 'pomarańczowy': 8, 'niebieski': 4}
```

Dwa ostatnie wiersze pokazują, że sumowanie przez `defaultdict(int)` i przez `Counter` daje ten sam wynik.

## Uwagi implementacyjne

Puste kontenery mają adnotacje typów, na przykład `policzone: dict[str, int] = {}`, `grupy: dict[int, list[str]] = {}` albo `ostatnie_trzy: deque[int] = deque(maxlen=3)`. Od razu widać, jakiego typu są klucze i wartości.

Notacja z nawiasami kwadratowymi jest wygodna, gdy masz pewność, że klucz istnieje. Gdy klucza może nie być, użyj `get` z wartością domyślną albo `defaultdict`.

W funkcji `zliczanie_grupowanie` wynik `len(slowo)` trafia do zmiennej `slowo_dl`, dzięki czemu `len` jest wywoływane raz dla każdego słowa.

Słownik pamięta kolejność dodawania par, dlatego klucze w wynikach zliczania i grupowania pojawiają się w kolejności, w jakiej pierwszy raz wystąpiły w danych.

Linia `c1["a"] += 3` jest zakomentowana, żeby dodawanie i odejmowanie obiektów `Counter` działało na wartościach z definicji `c1`.

Wywołanie `list(litery.elements())` zwraca każdą literę tyle razy, ile wynosi jej licznik, bez sortowania. Dopiero `sorted(litery.elements())` układa litery alfabetycznie.

Kolejność elementów w zbiorze nie jest gwarantowana, dlatego wyniki działań na zbiorach wypisuję przez `sorted`.