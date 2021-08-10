
from math import factorial
import string

def zad1(n):
  pass

  # pascal = []
  # for i in range(n-1):
  
  #   pascal.append([])
  #   pascal[i].append(1)
  #   for j in range(1,i):
  #     pass
  #   pascal[i].append(1)
  #     # pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])


  # for i in range(n):
  #   for j in range(n-i) :
  #     print(end = " ")


def zad2(n,k):
  if (n == 0 and k == 0) or k == 0:
      return 1.0
  elif n == k:
      return 0.0
  else:
      return (k+1)*zad2(n-1, k) + (n-k)* zad2(n-1,k-1)

def zad3(text, s):
  textReturn = ""
  for letter in text:
    if letter.isupper():
      textReturn += chr((ord(letter) + s - 65)%26 + 65)
    else:
      textReturn += chr((ord(letter) + s - 97)%26 + 97)
  return textReturn
