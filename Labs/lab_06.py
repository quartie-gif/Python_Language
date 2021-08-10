#1 

import time
import random as rand
import sys
import math
import functools as func

powt=1000
N=10000

def tester(fun):
  for _ in range(powt):
    fun(N)

def forStatement(num):
  temp = []
  for i in range(num):
    temp.append(i)

def listComprehension(num):
  temp = [i for i in range(num)]

def mapFunction(num):
  temp = map(lambda k: k, range(num))

def generatorExpression(num):
  temp = (i for i in range(num))


print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
  start = time.time_ns()
  print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
  end = time.time_ns()
  print(end - start)


# RESULTAT : 
# forStatement         => None
# 2062247387
# listComprehension    => None
# 981754866
# mapFunction          => None
# 943014
# generatorExpression  => None
# 988327




#2 

points_len = [math.sqrt(rand.uniform(-1,1)**2 + rand.uniform(-1,1)**2) for _ in range(N)]
print(len(list(filter(lambda x: x<=1 ,points_len)))/N*4)

#3 
#Proszę znaleźć:
# największą wartość w każdym wierszu macierzy (map),
# największą wartość w każdej kolumnie macierzy (map+zip),
# sumę dowolnej liczby macierzy macierzy (map+zip+lista składana)

A = [
  [1,2,8],
  [1,6,-2],
  [1,110,3]
]
B = [
  [1,2,3],
  [1,5,-2],
  [1,110,3]
]
C = [
  [1,4,8],
  [1,6,-2],
  [1,8,3]
]

print(list(map(max, A)))
print(list(map(max,(zip(*A)))))

# 4 Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako współrzędne punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym elementem jest lista x-ów, a drugim lista y-ów. Proszę to zrobić w jednej linijce korzystając z funkcji reduce, wyrażenia lambda oraz wbudowanej funkcji map (obie listy tworzymy jednocześnie!) (2p)
temp = [[rand.randint(1,10) , rand.randint(1,10)] for _ in range(9)]
print(temp)
print(list(zip(*temp)))



# 5 Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji wbudowanych reduce i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności (wzory w pliku) (2p)

def foo(x, y):
  n = len(x)
  x_sr = func.reduce(sum, x) / n
  # D = func.reduce(sum, y, x)


