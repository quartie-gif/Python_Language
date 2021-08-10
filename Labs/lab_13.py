import abc
import types
import random as rand

################################################
# Zad 1
################################################
class Calka(abc.ABC):
  '''Klasa abstrakcyjna Calka'''

  def __init__(self, begin, end, steps, fun):

    if not isinstance(begin, (float, int)) or not isinstance(end, (float, int)) or not isinstance(steps, (int)) or not isinstance(fun, types.FunctionType):
      raise TypeError
      
    self.begin = begin
    self.end = end
    self.steps = steps
    self.fun = fun

  @abc.abstractmethod
  def met(self):
    '''Metoda abstrakcyjna obliczajaca wartosc calki'''

class trapez_method(Calka):
  '''Klasa reprezentujaca metode trapezow'''

  def met(self):
    '''Definicja metody abstakcyjnej'''
    h = (self.end - self.begin)/self.steps
    s = 0 
    for i in range(1, self.steps + 1):
      s += self.fun(self.begin + i*h) + self.fun(self.begin + (i+1)*h)
    return h/2 * s

class simpson_method(Calka):
  '''Klasa reprezentujaca metode Simpsona'''

  def met(self):
    '''Definicja metody abstakcyjnej'''
    h = (self.end - self.begin)/(2 * self.steps)
    s_even = s_odd = 0 
    for i in range(1, 2 * self.steps):
      if i % 2 == 0:
        s_even += self.fun(self.begin + i*h)
      else:
        s_odd += self.fun(self.begin + i*h)
      
    return h/3 * (self.fun(self.begin) + 4 * s_odd + 2 * s_even + self.fun(self.end)) 

################################################
# Zad 2
################################################

class Stack:
  def __init__(self, existing = None):
    self.values = []
    if isinstance(existing, Stack):
      self.values.extend(existing.values)


  def add(self, val):
    self.values.append(val)
    return self
  
  def remove(self):
    self.values.pop()
    return self

  def add_from(self, s):
    if isinstance(s, Stack):
      self.values.extend(s.values)
    return self


  def size(self):
    return len(self.values)


  def print(self):
    print('Printing stack : ', end = "")
    for el in self.values:
      print(str(el), end = " ")
    print()

class Stack_sorted(Stack):
  def __init__(self, existing = None):
    self.values = []
    if isinstance(existing, (Stack, Stack_sorted)):
      self.values.extend(existing.values)
      self.values.sort()

  def add_from(self, s):
    if isinstance(s, Stack_sorted) and self.values[-1] >= s.values[0]:
      self.values.extend(s.values)




################################################
# Main Funcition 
################################################
if __name__ == '__main__':

  #testing Integral

  obj_1 = trapez_method(1, 100, 100, lambda x: x)
  print(obj_1.met())
  obj_2 = simpson_method(1, 100, 100, lambda x: x)
  print(obj_2.met())


  # testing Stack
  stack_1 = Stack()
  stack_1.add(11).add(12).remove().add(14).print()

  stack_2 = Stack()
  for _ in range(100):
    stack_2.add(rand.randint(0, 101))
  stack_2.print()

  srednia = 0 
  for el in stack_2.values:
    srednia += el
  print(f"Srednia wynosi: {srednia/stack_2.size()}")