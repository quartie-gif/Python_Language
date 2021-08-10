def zad1(file, n):
  print("------------------ZADANIE 1------------------")
  with open(file, "r") as f:
    temp = f.readlines()
  print("\n n początkowych wierszy pliku \n", temp[:n])
  print("\n n końcowych wierszy pliku \n", temp[-n:])
  print("\n co n-tego wiersza pliku \n",temp[:: n])
  print("\n n-tego słowa ze wszystkich wierszy   \n", [line.split(" ")  for line in temp]) #   
  print("\n n-tego znaku ze wszystkich wierszy\n", list(line[n-1] for line in temp)) 


zad1("data/data0.in", 3)


# Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
# pierwsza kolumna - numer wiersza,
# druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
# trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)

import numpy
import glob

# print(dir(glob))
# help(glob)

# print(list(glob.glob("data/data*.in")))

def zad2():
  print("------------------ZADANIE 2------------------")
  FirstCol = []
  SecondCol = []
  ThirdCol = []
  dic = {}
  k = 0
  for file in glob.glob("data/data*.in"):
    with open(file) as f:
      FirstCol.append(k)
      temp = f.readlines()
      for line in temp:
        SecondCol.append([line.split(" ")[0]])
      k = k+1
      print(k)
      print(list(SecondCol))
  with open("Output_Zad2.txt", "a") as out2:
    for _ in range(1, k):
      out2.write(f"nr. {k}, {SecondCol[k]}, {ThirdCol[k]} \n")

# zad2()

def zad3():
  print("------------------ZADANIE 3------------------")
  file = open("Zad3_instrukcja.txt", "w")
  file.writelines('''
  import matplotlib.pyplot as plt
  import numpy

  

  x,y,dy=numpy.loadtxt("Output_Zad2.txt", unpack=True)
  #wyrysowanie krzywej y(x), 'o' oznacza styl punktu
  plt.plot(x, y, 'o')
  #wyrysowanie krzywej y(x) wraz z niepewnościami 
  plt.errorbar(x, y, marker='*', yerr=dy)
  #opis osi
  plt.xlabel('x')
  #zapis do pliku, format określony przez rozszerzenie w nazwie
  plt.savefig('res.pdf')



 
  ''')
  
  

  file.close()
  file = open("Zad3_instrukcja.txt", "r")
  for line in file:
    print(line)
  file.close()
  

# Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób, w kolejnych latach. Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się "nazwisko", kolejne kolumny będą odpowiadały pozycja danej osoby na liście rankingowej w kolejnych latach, od 2000 do 2020 (2.5p)

zad3()

def zad4():
  print("------------------ZADANIE 4------------------")
  dic = {}
  for file in glob.glob("rank/*.txt"):
    with open(file) as f:
      temp = f.readlines()
      for line in temp:
        dic.setdefault(line.split(" ")[0].strip(), []).append(line.split(" ")[1].strip())
  print(dic)

  file = open("zad4.txt", "w")
  for dic in dic.items():
    file.write(f"Name: {dic[0]}, Miejsca: {dic[1]}\n")
  file.close()
  file = open("zad4.txt", "r")
  for line in file:
    print(line)
  file.close()

zad4()
