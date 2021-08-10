#Zad1 
# Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
# Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy, mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku

# key - ile elementow nei zmienilo swojej pozycji
# value - ile razy zadany klucz sie zdarzyl

import random as rand

k = 11
dic = {}
counter = 0
key = 0
list_1 = [rand.randint(0,5*k) for i in range(k)]


for i in range(100):

  list_temp = list_1[:]
  rand.shuffle(list_temp)

  for i in range(len(list_temp)) :
    if list_temp[i] == list_1[i]:
      counter += 1
    
  
  if counter in dic:
    dic[counter] +=1 
  else :
    dic[counter] = 1

  counter = 0
  
  
  

print("Lista wylosowanych wartosci to : ", list_1)
print("\nWygenerowany przez nas slownik to : ", dic)
# print(dir(rand))

# Zad 2
# Proszę utworzyć losowy string o długości k zawierający tylko małe litery, pomiędzy poszczególne litery proszę wstawić kropkę

# Szukanie wartosci ascii print(chr(97), chr(122))

rand_str = ""

for i in range(k) : 
  rand_str += chr(rand.randint(97,122)) + '.'

print("\nWygerenowany losowo napis :", rand_str)

# Zad 3
# Proszę utworzyć listę stu wartości losowych z przedziału [0,20). Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są liczbami z listy, a wartościami lista ich indeksów.
# w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate (1.5p)
# w rozwiązaniu proszę wykorzystać metody setdefault i index (1.5p)

list_1 = [rand.randint(0,20) for i in range(100)]
list_2 = [rand.randint(0,20) for i in range(100)]

print("\nLista pierwsza : " , list_1)
print("\nLista druga : " , list_2)

dic_1 = {}
dic_2 = {}

# enumerate()
for index, val in enumerate(list_1):
  dic_1.setdefault(val,[]).append(index)

# index()

list_copy = list_1[:]

for val in list_1:
  dic_2.setdefault(val,[]).append(list_copy.index(val))
  list_copy.remove(val)

print("\nSłownik pierwszy : ", dic_1)
print("\nSłownik drugi  : ", dic_2)


# Zad 4
# Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych składających się z n cyfr, gdzie n jest z przedziału [3,6], jest liczbami palindromowymi. Wynik proszę zapisać w słowniku (2p)

list_temp = []
n = rand.randint(3,7)
for i in range(1000):
  list_temp.append(rand.randint(10**(n-1),10**n))

print("\nn jest równe : ", n)

print("\nLista wylosowanych wartości z przedziału ({}, {}) to : {}".format(10**(n-1),10**n, list_temp))

counter = 0
for i in range(1000):
  pass



# Zad 5

# Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne liczby naturalne, a wartościami liczby losowe z przedziału [1,100). Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami.
# Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze są kluczami występującymi jednocześnie w obu wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości związanych z danym kluczem w słownikach oryginalnych  (2p)


# dic_3 = {abs(rand.randint(1, 100) : f'{k}' for k in range(10)}
# dic_4 = {abs(rand.randint(1, 100) : f'{k}' for k in range(10)}







