[Polski](README.md) · **English**

---

# Matura - Computer Science, extended level, Python course, part 9. "Containers: dict, set, deque"

> ### 🎬 Video walkthrough
> A full step-by-step walkthrough of this material is available on my YouTube channel:
> **[Link to the video on YouTube](https://youtu.be/zeLSmTVsogI)**
>
> In the video I create dictionaries in several ways and show how to count and group data. I also cover the `Counter` and `defaultdict` types from the `collections` module, `set` and the `deque` queue. At the end I sum up when to use which container.

---

## Table of contents

- [Description](#description)
- [Requirements](#requirements)
- [How to run](#how-to-run)
- [Project structure](#project-structure)
- [Topics covered](#topics-covered)
- [Compliance with exam rules](#compliance-with-exam-rules)
- [When to use which container](#when-to-use-which-container)
- [Results](#results)
- [Implementation notes](#implementation-notes)

## Description

Code for part 9 of my Python course, which prepares students for the Matura exam in Computer Science at the extended level. This part wraps up the topic of containers. After lists and tuples, it is time for the `dict` dictionary, its special variants `Counter` and `defaultdict`, the `set` and the `deque` queue.

A dictionary stores key and value pairs. You read a value by its key quickly, without searching the whole structure. In a list, when you do not know the position of the element you are looking for, you have to go through the elements one by one. In a dictionary you simply ask whether a given key exists.

In the Matura exam, a dictionary is used mainly for two things: counting occurrences and grouping data by a common feature. That is why I first show both operations on a regular dictionary, and then with `Counter` and `defaultdict`, which make them simpler.

All the new code from this video is in the `app-9-kontenery-dict.py` file. The other files come from earlier parts of the course. The next video covers strings.

## Requirements

- Python 3.10 or newer. The `app-4-instrukcje-warunkowe.py` file uses the `match` statement, available since Python 3.10. The `app-9-kontenery-dict.py` file uses the `|` operator to merge dictionaries and type annotations such as `dict[str, int]`, which work since Python 3.9.
- No external dependencies. Only the standard library is used, namely the `collections`, `random` and `math` modules.

## How to run

```bash
git clone https://github.com/kmprograms/matura-kurs-python-9-kontenery-dict-set-deque
cd matura-kurs-python-9-kontenery-dict-set-deque
python app-9-kontenery-dict.py
```

Each topic from the video is wrapped in a separate function. The `main` function calls only one of them at a time, and the other calls are commented out:

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

To run a different example, uncomment the chosen call in `main`. Files from earlier parts of the course are run the same way, for example `python app-8-kontenery-tuple.py`.

## Project structure

| File | Description |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | First program, variables, f-strings, arithmetic operators and type conversion |
| `app-2-liczby-calkowite.py` | Integer operations, the `//` and `%` operators, comparison operators, logical operators, digits of a number |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Reading input with `input` (commented out), the `random` module, number systems, bitwise operations, the `math` module |
| `app-4-instrukcje-warunkowe.py` | `if`, `elif`, `else` statements, conditional expression, the `match` statement, the `min`, `max` and `abs` functions |
| `app-5-petle.py` | `while` and `for` loops, `range`, `break`, `continue`, nested loops |
| `app-6-funkcje.py` | Functions, parameters, default and keyword arguments, `return`, returning multiple values, the `main` function |
| `app-7-kontenery-listy.py` | Lists, list methods, slicing, two-dimensional lists, list comprehensions and generator expressions |
| `app-8-kontenery-tuple.py` | Tuples and `namedtuple` |
| `app-9-kontenery-dict.py` | Code from this video: dictionaries, `Counter`, `defaultdict`, sets and `deque` |

## Topics covered

### Creating a dictionary and basic operations

The `slowniki_podstawy` function. A dictionary can be created in several ways: with curly braces, with keyword arguments of the `dict` function, from two lists combined with `zip`, or from a list of tuples. All four ways produce the same dictionary, which the comparison `d1 == d2 == d3 == d4` confirms.

```python
d1 = {"one": 1, "two": 2, "three": 3}
d2 = dict(one=1, two=2, three=3)
d3 = dict(zip(["one", "two", "three"], [1, 2, 3]))
d4 = dict([("one", 1), ("two", 2), ("three", 3)])
d5: dict[str, int] = {}
```

Keys are unique and must be immutable, for example numbers, strings or tuples. Values can be anything, including lists and other dictionaries. The `len` function returns the number of pairs in the dictionary.

Reading values:

- `oceny["Jan"]` returns the value stored under the key and raises a `KeyError` for a missing key
- `oceny.get("Ewa")` returns `None` for a missing key
- `oceny.get("Ewa", 0)` returns the default value `0` for a missing key

A dictionary is mutable, just like a list. The assignment `oceny["Ewa"] = 3` adds a new pair, and `oceny["Jan"] += 1` changes an existing value. `del` removes a pair, and `in` checks whether a key exists. `pop` removes a pair and returns its value, and with a second argument it returns a default value when the key is missing. `setdefault` returns the value under an existing key or inserts a new pair when the key is missing.

Merging dictionaries:

```python
d7 = {"a": 1, "b": 2}
d8 = {"b": 3, "c": 4}
print(d7 | d8)  # {'a': 1, 'b': 3, 'c': 4}
print({**d7, **d8})
```

In both forms, when a key repeats, the value from the right-hand dictionary wins, and new keys from the right-hand dictionary go to the end of the result.

### Iterating over a dictionary

The `przegladanie_slownika` function. A `for` loop over a dictionary yields its keys. The `items()` view yields pairs, which you unpack straight into two variables:

```python
for imie, pensja in pensje.items():
    print(f"{imie=}, {pensja=}")
```

The `keys()` and `values()` views return only the keys or only the values. The `list` function turns them into a regular list.

### Counting and grouping with a regular dictionary

The `zliczanie_grupowanie` function. Counting name occurrences using `get` with the default value `0`:

```python
for imie in imiona:
    policzone[imie] = policzone.get(imie, 0) + 1
```

Result: `{'adam': 3, 'ewa': 1, 'iza': 2}`.

Grouping words by their number of characters. When a key does not exist yet, you first have to create an empty list under it:

```python
for slowo in slowa:
    slowo_dl = len(slowo)
    if slowo_dl not in grupy:
        grupy[slowo_dl] = []
    grupy[slowo_dl].append(slowo)
```

Result: `{3: ['kot', 'lis', 'osa'], 4: ['pies', 'mysz'], 2: ['ul']}`.

### Key with the largest value and sorting

The `klucz_z_najwieksza_wartoscia` function. I show three approaches to finding the maximum in the dictionary `{"adam": 3, "ewa": 1, "iza": 2}`:

1. `max(liczniki, key=lambda k: liczniki[k])` returns the key with the largest value
2. `max(liczniki.items(), key=lambda pair: pair[1])` returns the whole pair, which you unpack into two variables
3. `max(liczniki.values())` finds the largest value, and a list comprehension collects all keys that have it

Sorting pairs by value, in descending order:

```python
print(sorted(liczniki.items(), key=lambda pair: pair[1], reverse=True))
```

Result: `[('adam', 3), ('iza', 2), ('ewa', 1)]`. The `min` function is used the same way as `max`.

### Dictionary comprehensions

The `wyrazenia_slownikowe` function. Just as a list comprehension creates a new list, a dictionary comprehension creates a new dictionary. The data source can be a list, another dictionary or `range`:

```python
imiona = ["ala", "ola", "pawel", "zosia"]
print({imie: len(imie) for imie in imiona if len(imie) > 3})

d = {"a": 1, "b": 2, "c": 3}
print({k: v for k, v in d.items() if v < 3})
print({n: n ** 2 for n in range(1, 6)})
```

Results in order: `{'pawel': 5, 'zosia': 5}`, `{'a': 1, 'b': 2}` and `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`.

### Counter and defaultdict

The `typy_podobne_do_dict` function. Both types come from the `collections` module and make counting and grouping simpler.

`Counter` counts occurrences of list elements or characters of a string in a single call. `dict(cnt1)` turns the result into a regular dictionary. The `most_common()` method returns pairs sorted in descending order by the number of occurrences, and `most_common(n)` returns only the `n` most common ones:

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

The `elements()` method returns each element as many times as its count. `Counter` objects can also be added and subtracted:

```python
c1 = Counter(a=1, b=5, c=4)
c2 = Counter(a=3, b=1, d=5)

# c1["a"] += 3
# print(c1)

print(c1 + c2)
print(c1 - c2)
```

When adding, the counts of matching keys are summed. When subtracting, only keys with a positive count remain in the result.

`defaultdict` creates a default value for a missing key on its own. `defaultdict(list)` creates an empty list, and `defaultdict(int)` creates the value `0`. Thanks to this, grouping no longer requires checking the key with an `if` statement:

```python
grupy1: defaultdict[str, list[int]] = defaultdict(list)
for kolor, liczba in pary:
    grupy1[kolor].append(liczba)
```

You can sum values by key with `defaultdict(int)` or with `Counter`, and the result is the same. `Counter` additionally offers methods such as `most_common`.

```python
sumy: defaultdict[str, int] = defaultdict(int)
for kolor, liczba in pary:
    sumy[kolor] += liczba
print(dict(sumy))
```

### Sets

The `zbiory` function. A set stores elements without duplicates. It has no order and no indexes, so reading by index and slicing do not work. Checking whether an element belongs to a set is very fast, regardless of the size of the set. Set elements must be immutable.

In the code I show:

- removing duplicates from a list with `set(imiona)` and from a string with `set("kmprograms")`
- the `add`, `remove` (raises `KeyError` when the element is missing) and `discard` (no error) methods
- the set comprehension `{n % 10 for n in [12, 22, 35, 41, 52]}`
- creating an empty set with `set()`, because `{}` creates an empty dictionary
- set operations

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

Meaning of the operators and results:

- `a | b` - union: `[11, 22, 33, 44]`
- `a & b` - intersection: `[22, 33]`
- `a - b` - difference, where the order of the sets matters: `[11]`
- `a ^ b` - symmetric difference, meaning elements present in only one of the sets: `[11, 44]`
- `{22} <= a`, `{22, 33} < a` and `a == {33, 22, 11}` - set comparisons, all of them give `True`, because order does not matter in sets
- `a.isdisjoint({1, 2})` - checks whether the sets have no common elements: `True`

### The deque queue

The `kolejki` function. `deque` from the `collections` module lets you add and remove elements at both ends quickly. A list does this quickly only at the end. The `pop` with zero and `insert` with zero operations on a list shift all remaining elements, so they are slow for large lists.

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

Output:

```
deque([0, 1, 2, 3, 4])
4
0
deque([1, 2, 3])
deque([3, 1, 2])
deque([1, 2, 3])
```

A queue with the `maxlen=3` parameter holds at most three elements. After adding the numbers `5, 6, 7, 8`, only `6, 7, 8` remain and the five drops out. Finally, `list(ostatnie_trzy)` turns the queue into a regular list. Later in the course, when we get to algorithms, I will show how to build a stack with `deque`.

## Compliance with exam rules

In the Matura exam, whenever the task does not explicitly forbid something, you can use everything the Python standard library provides. `Counter`, `defaultdict` and `deque` come from the `collections` module, which is part of it. So you can use them, for example, when counting data read from a file. If you prefer to stick with a regular dictionary, you can write counting and grouping the way it is done in the `zliczanie_grupowanie` function.

## When to use which container

I wrote the summary from the end of the video in the docstring inside the `main` function:

| Container | When to use it |
| --- | --- |
| `list` | When data has to be processed in order, appended, removed or sorted. It is the default choice when reading consecutive lines from a file. |
| `tuple` | When several values form one immutable record, for example a pair of coordinates. A tuple is also useful when a function returns several results or when you need a composite dictionary key. A tuple is immutable, and dictionary keys must be immutable too. |
| `namedtuple` | When a record has several fields and you want to access them by name instead of by index. The code becomes more readable, for example `wiersz.wynik` instead of `wiersz[2]`. |
| `dict` | When a value has to be read quickly by key, for example a score by surname. It also works well for counting and grouping data. |
| `Counter` | When you need to count how many times each element occurs. The `most_common()` method immediately returns the most common elements. |
| `defaultdict` | When you group or sum data by key and do not want to check every time whether the key already exists. For a missing key it creates a default value on its own, for example an empty list or zero. |
| `set` | When only unique elements matter or when you check many times whether an element occurs in the data. It is also useful for set operations such as intersection and difference. |
| `deque` | When you add or remove elements at both ends, that is for a queue or a stack. The `rotate()` method performs a cyclic shift. |

## Results

In the current version of the file, the `main` function calls `typy_podobne_do_dict`. After running `python app-9-kontenery-dict.py`, the program prints:

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

The last two lines show that summing with `defaultdict(int)` and with `Counter` gives the same result.

## Implementation notes

Empty containers have type annotations, for example `policzone: dict[str, int] = {}`, `grupy: dict[int, list[str]] = {}` or `ostatnie_trzy: deque[int] = deque(maxlen=3)`. You can see the types of keys and values right away.

Square bracket notation is convenient when you are sure the key exists. When the key may be missing, use `get` with a default value or `defaultdict`.

In the `zliczanie_grupowanie` function, the result of `len(slowo)` is stored in the `slowo_dl` variable, so `len` is called once per word.

A dictionary remembers the order in which pairs were added, which is why keys in the counting and grouping results appear in the order in which they first occurred in the data.

The line `c1["a"] += 3` is commented out so that adding and subtracting `Counter` objects works on the values from the definition of `c1`.

The call `list(litery.elements())` returns each letter as many times as its count, without sorting. Only `sorted(litery.elements())` puts the letters in alphabetical order.

The order of elements in a set is not guaranteed, which is why I print the results of set operations with `sorted`.