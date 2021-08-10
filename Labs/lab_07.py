# Zad1 

def gen1(num):
  number = 0
  while number <= num:
    yield number
    number += 1


def gen2(s):

  for el in s:
    if sum(j for j in range(1, int(el/2) + 1) if el%j == 0) == el and el != 0:
      yield el

def gen3(s, stop):
  for el in s:
    if el == stop:
      break
    yield el


# print(list(gen1(25)))
# print(list(gen2(list(gen1(10000)))))
# for el in gen3([1,3,4,2,5,2,101,3,2], 101):
#   print(el)
# print("Lista liczb doskonałych dla n = 10000 :" )
# print(list(gen2(gen1(10000))))

# zad 2 
import math

def zad2():
  a =0.05
  i = 0
  u = 0
  x_0 = 1
  x = 1
  while True:
    i += 1 
    u += a/x
    x = x_0 +i*a
    yield x, u, math.log(x)
    if x >= 1.5:
      break  
  
for el in zad2():
  print(el)


# Zad 3 

def zad3(n):
  for j in range(n, 1, -1):
    l = []
    x = n
    for k in range(j-1, 0, -1):
      while True:
        if x >= k:
          l.append(k)
          x -= k
        else:
          break
    yield l
      
      
for i in zad3(13):
  print(i)

# zad 4

import random

def zad4():
  val = random.uniform(0,1)
  while True:
    val2 = val
    val = random.uniform(0,1)
    if val < 0.1:
      break
    delta = abs(val2 - val)
    if (delta > 0.4):
      yield val

for i in zad4():
  print(i)

# zad 5 
# 
# Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych (2p)
# Do testów: range(8), range(-8), range(1,8), range(8,1), range(1,8,2), range(1,8,-2), range(8,1,2), range(8,1,-2)

# def zad5(start, stop = 0, step = 1):
#   if start > stop:
#     while start > stop:
#       yield start
#       start -= step
#     return 
  
#   if start < stop:
#     while start < stop:
#       yield start
#       start += step

# for i in zad5(8,1,-2):
#   print(i)
      
