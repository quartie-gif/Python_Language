#Testowane dla argumentow : 32 f sdsvdFS f#S542 ao 
# python3 main.py 32 f sdsvdFS f#S542 ao 


# Zad 1
# Proszę utworzyć string składający się z elementów listy argv z wyłączeniem nazwy programu. Jeżeli program został uruchomiony bez podania parametrów proszę wypisać na ekran komunikat informujący o właściwym sposobie uruchomienia programu (1p)

import sys

if len(sys.argv) == 1:
  print("Wrong number of arguments!!!")
else:
  arr=''.join(sys.argv[1:])
print(arr)


# Zad 2
# Na podstawie wcześniej utworzonego stringa proszę utworzyć cztery listy: zawierającą małe litery, zawierającą duże litery, zawierającą cyfry oraz zawierającą wszystko co nie jest literą (2p)

lower = []
upper = []
digits = []
noletters = []

for i in arr:
  if i.isalpha():
    if i.islower():
      lower.append(i)
    else :
      upper.append(i)
  elif i.isdigit():
    digits.append(i)
  else:
    noletters.append(i)


print("Lower letters : {}\nUpper letters: {}\nDigits : {}\nNoletters : {}".format(lower, upper, digits, noletters))



# Zad 3 
# Na podstawie utworzonej listy zawierającej małe litery proszę utworzyć listę małych liter bez powtórzeń. Następnie proszę utworzyć nową listę, w której każdy element jest dwuelementową krotką (litera, krotność jej wystąpienia w liście oryginalnej) (2p)

lower_2 = []

for i in lower:
  if i not in lower_2 :
    lower_2.append(i)
print("Lista elementów unikalnych :",lower_2)

uniq = [(letter, lower.count(letter)) for letter in lower_2]
print("Lista krotek (listera, krotnosc wystapienia :)", uniq)


# Zad 4 
# Otrzymaną w powyższym punkcie listę proszę wyświetlić w kolejności od najwyższej krotności (1p)


# help(uniq)
uniq.sort(reverse = True, key = lambda el: el[1])
print("Lista w kolejności od najwyższej krotności : ", uniq)


# Zad 5
# Proszę utworzyć listę dwuelementowych krotek, w których pierwszy element jest liczbą pobraną z listy cyfr, drugi natomiast wartością funkcji liniowej ax+b dla danej liczby; wartości współczynników proszę ustalić w następujący sposób: a równa się liczbie samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże (2p)

samogloski = ['a', 'o', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


sam_counter = 0
sp_counter = 0
temp = lower + upper
for i in temp:
  if i in samogloski:
    sam_counter += 1
  else:
    sp_counter += 1


a = sam_counter
b = sp_counter
print("Ilosc samoglosek : {}\nIlosc spolglosek : {}".format(a,b))
temp_krotka = [(float(i), a*float(i) + b)for i in digits]

print("Lista dwuelementowych krotek (x, y(x) = ax + b) : ",temp_krotka)

# Zad 6
# Proszę obliczyć wartości parametrów prostej korzystając z metody najmniejszych kwadratów (2p):

x_sr = 0
y_sr = 0
D = 0
a = 0 
b = 0

# licze x sredni
for i in temp_krotka:
  x_sr += i[0]
x_sr = x_sr / len(temp_krotka)

# licze y sredni
for i in temp_krotka:
  y_sr += i[1]
y_sr = y_sr / len(temp_krotka)

# licze D 
for i in temp_krotka:
  D += (i[0] - x_sr)**2

#lcize a
for i in temp_krotka:
  a += i[1]*(i[0] - x_sr)
a = a/D

#lcize b
b = y_sr -a*x_sr

print("x_sr : ",x_sr)
print("y_sr : ",y_sr)
print("D : ",D)
print("a : ",a)
print("b : ",b)