import random
import math
import matplotlib.pyplot as plt

# Zad 1
class IFS:

  def __init__(self, trans = (), prob = (), point = (0,0)):
    self.x = [point[0]]
    self.y = [point[1]]
    self.trans = trans
    self.prob = prob

  def transition(self, iter_num):
    for i in range(iter_num):
      trans_factor = random.choices(self.trans, self.prob)[0]
      self.x.append(self.x[i]* trans_factor[0] + self.y[i] * trans_factor[1] + trans_factor[2])
      self.y.append(self.x[i]* trans_factor[3] + self.y[i] * trans_factor[4] + trans_factor[5])
    
  def print(self):
    plt.plot(self.x, self.y, '.')
    plt.show()

class Vector:

  def __init__(self, x = .0, y = .0, z = .0):
    self.x = x
    self.y = y
    self.z = z

# metoda str
  def __str__(self):
    return f"Vector(x, y, z): ({self.x}, {self.y}, {self.z})"

# Dodawanie
  def __add__(self, p):
    return Vector(self.x + p, self.y + p, self.z + p)

# Odejmowanie 
  def __sub__(self, p):
    return Vector(self.x - p, self.y - p, self.z - p)

# Mnozenie
  def __mul__(self, p):
    return Vector(self.x * p, self.y * p, self.z * p)

  def lenVec(self):
    '''Metoda zwracajaca dlugosc'''
    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


  def dot_prod(self, v2):
    '''Metoda zwracajaca iloczyn skalarny'''
    return self.x * v2.x + self.y * v2.y + self.z * v2.z  

  def vector_prod(self, v2):
    '''Metoda zwracajaca iloczyn wektorowy'''
    return Vector(self.y * v2.z - self.z * v2.y, self.x * v2.z - self.z * v2.x, self.x * v2.y - self.y * v2.x)

  def triple_prod(self, v2, v3):
    '''Metoda zwracajaca iloczyn mieszany'''
    return self.dot_prod(v2.vector_prod(v3))

# ------------------ FUNKCJE ------------------

def magnetic_induction(B, S):
  '''strumien indukcji magnetycznej'''
  return B.vector_product(S)

def Lorentz_force(q, v, B, E):
  '''sila Lorentza'''
  return (v.vector_prod(q)+ E)*q

def work_Lorentz_force(q, E, v):
  '''praca sily Lorentza'''
  return E.dot_product(v)*q


if __name__ == "__main__":

  # Zad 1
  # obj = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
  # obj.transition(1000)
  # obj.print()

  # Zad 2
  vec1 = Vector(1.0, 3.0, 3.0)
  vec2 = Vector(2.0, 3.0, 3.0)
  vec3 = Vector(1.0, 6.0, 5.0)

  print(vec1.dot_prod(vec2))
  print(vec1.vector_prod(vec2))
  print(vec1.triple_prod(vec2, vec3))

  # Zad 3 

