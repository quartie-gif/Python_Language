# Zad 1 
# Proszę napisać funkcję przyjmującą jako parametr string (przy wywołaniu będziemy przekazać argument wiersza poleceń). Zakładamy, że string ten zawiera poprawną definicję wyrażenia/funkcji matematycznej z jedną zmienną x, czyli np. 'a*x+b', 'a*x**2+b*x+c'. W miejscu wszystkich stałych proszę wstawić losowe liczby całkowite z przedziału [0,10), proszę wykorzystać metodę translate. Z funkcji proszę zwrócić listę dwuelementowych krotek (x, f(x)), dla 10 losowych liczb rzeczywistych z przedziału [0,1] (2p).

import sys
import random as rand

# funkcja przyjmującą jako parametr string zwracająca listę krotek (x, f(x))

def foo(expression, letters):
  dic = {}
  for i in letters:
    dic[ord(i)] = ord(str(rand.randint(0,9)))
  exp = expression.translate(dic)
  print(exp)
  l = [(rand.random(), eval(exp)) for x in range(10) ]
  return l

# szukamy liter
_letters = []

for i in sys.argv[1]:
  if i.isalpha() and not i =='x' : 
    _letters.append(i)
print("List znalezionych liter: ", _letters)
print("Lista krotek (x, f(x)): ", foo(sys.argv[1], _letters))


# Zad 2

# Proszę napisać funkcję, do której można przekazać zmienną liczbę parametrów, zwracającą listę. Do wynikowej listy trafiają elementy, które powtarzają się we wszystkich parametrach przekazanych do funkcji, np. ([1,2,3], (1,3,5), [3,2]) -> [3], ([1,2,3], (1,3,5), [3,2,1]) -> [1,3].
# Proszę użyć konstrukcji for-else (2p)

def fun(*l):

  prev = set()
  for i in l:
    for j in range(len(i)):
      for k in l:
        if i[j] == k[j]:
          prev.add(i[j])
        

  else:
    print("Wartosci w tablicach :", prev)

fun([1, 2, 3], [3, 4, 5])

# Zad 3

#Proszę napisać funkcję przyjmującą dwie sekwencje i parametr z wartością domyślną True. Funkcja zwraca listę dwuelementowych krotek zawierających elementy o tych samych indeksach z obu sekwencji. Jeżeli wartość trzeciego parametru wynosi True, długość zwracanej listy równa jest długości krótszej z przekazanych sekwencji, w przeciwnym wypadku brakujące elementy w krotkach uzupełniamy wartością None. Budowanie każdej z wynikowych list jedna linijka, proszę nie używać funkcji wbudowanych! (2p)  

