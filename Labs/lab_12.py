import math
from scipy.misc import derivative
import random

##########################################
# Zad1
##########################################

class Fibo:
  def __init__(self, stop):
    self.value_1 = 0
    self.value_2 = 1
    self.stop = stop

  def __iter__(self):
    return Fibo(self.stop)#self
  
  def __next__(self):
    if self.value_1 >= self.stop:
      raise StopIteration 
    self.value_1, self.value_2 = self.value_2, self.value_1 + self.value_2
    return self.value_1


##########################################
# Zad2
##########################################

class pseudoGenerator:
  def __init__(self, start):
    self.m = 2**31-1
    self.a = 7**5
    self.c = 0
    self.value = start # x_0
    self.iter =0 

  def __iter__(self):
    return self
  
  def __next__(self):
    self.iter = self.iter + 1 
    self.value = (self.value * self.a + self.c) % self.m
    return self.value / self.m


##########################################
# Zad3
##########################################

class NewtonRaphson:
  def __init__(self, f):
    self.value = 1.5
    self.eps=10**(-5)
    self.f=f

  def __iter__(self):
    return self
  
  def __next__(self):
    if abs(self.f(self.value)) < self.eps:
      raise StopIteration 
    self.value = self.value - self.f(self.value)/derivative(self.f, self.value)
    return self.value


##########################################
# Main Function
##########################################

if __name__ == "__main__":
  # help(random.uniform)
  # help(derivative)

  # ex1 = Fibo(100)
  # for i in ex1:
  #   for j in ex1: 
  #     print(f"{i}, {j}")

  ex2 = pseudoGenerator(1)
  ile = 0
  for i in range(10**5):
    x,y=next(ex2),next(ex2)
    n = random.randint(0,10)
    bok = 0.1 * n
    pole = bok * bok
    if x*y <pole:
      ile = ile + 1 
  print(ile)

  # ex3 = NewtonRaphson(lambda x: math.sin(x) - (0.5 * x)**2)
  # for i in ex3:
  #     print(f"{i}")

 