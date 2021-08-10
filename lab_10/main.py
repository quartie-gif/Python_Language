import datetime

# ------------------------ ZAD 1 ------------------------
def controlSum(evidenceNumber):

  sumVal = 0.0
  wage = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

  sumVal = sum(map(lambda x: x[0]*int(x[1]), tuple(zip(wage, evidenceNumber))))
  sumVal %= 10
  sumVal = 10 - sumVal
  sumVal %= 10

  return sumVal

def zad1(evidenceNumber, date, sex):
  if len(evidenceNumber) != 11:
    raise ValueError(f"Podano nieprawidlowy pesel o dlugosci innej niz oczekiwano(11) : {len(evidenceNumber)}!!!")
  if sex != 'k' and sex != 'm':
    raise ValueError(f"Podana plec jest bledna!!!")
  if date.day != int(evidenceNumber[4:6]):
    raise ValueError(f"Podany dzien jest bledny!!!")

  if  1800 <= date.year < 1900 and date.month + 80 != int(evidenceNumber[2:4]):
    raise ValueError(f"Podany miesiac jest bledny: {evidenceNumber[2:4]} !!!")

  if  1900 <= date.year < 2000 and date.month + 0 != int(evidenceNumber[2:4]):
    raise ValueError(f"Podany miesiac jest bledny: {evidenceNumber[2:4]} !!!")

  if  2000 <= date.year < 2100 and date.month + 20 != int(evidenceNumber[2:4]):
    raise ValueError(f"Podany miesiac jest bledny: {evidenceNumber[2:4]} !!!")

  if  2100 <= date.year < 2200 and date.month + 40 != int(evidenceNumber[2:4]):
    raise ValueError(f"Podany miesiac jest bledny: {evidenceNumber[2:4]} !!!")

  if  2200 <= date.year < 2300 and date.month + 60 != int(evidenceNumber[2:4]):
    raise ValueError(f"Podany miesiac jest bledny: {evidenceNumber[2:4]} !!!")

  if date.year != evidenceNumber[:2]:
    raise ValueError(f"Podany rok jest bledny!!!")
  
  if int(evidenceNumber[6:10]) % 2  == 0 and sex == 'm':
    raise ValueError(f"Liczba porzadkowa jest bledna!!!")

  if int(evidenceNumber[6:10]) % 2  == 1 and sex == 'k':
    raise ValueError(f"Liczba porzadkowa jest bledna!!!")

  if controlSum(evidenceNumber) != evidenceNumber[10]:
    raise ValueError(f"Suma kontrolna jest bledna!!!")


# ------------------------ ZAD 2 ------------------------
def zad2():
  with open('daty.in') as f:
    pass
# ------------------------ ZAD 3 ------------------------
def zad3(N):
  l=[3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17,3,4,5]
  # l=[1,2,3,4,5,6,7,8,9]
  # l=[1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2]

  if len(l)%N != 0:
    raise ValueError(f"Funkcji nie da sie zrealizowac dla N= {N}, bo dlugosc listy to: {len(l)}")


  for i in range(0 ,len(l), N):
    suma = 0
    for j in range(i, i + N-1):
      suma += pow(l[j], 2)
    print(suma ,pow(l[i+N-1],2))
    if suma == pow(l[i+N-1],2):
      print("Znaleziono: ",l[i:i+N])
      print("Nieparzyste : ",list(filter(lambda x: x%2, l[i:i+N])))
      print("Parzyste : ",list(filter(lambda x: x%2 == 0, l[i:i+N])))
      
 

if __name__ == '__main__':
  # help(datetime)
  # print(controlSum('02070803628'))
  try:
    zad1('02060803618', datetime.date(1902,7,8), 'k')
    zad1('02270803624', datetime.date(2002,7,8), 'k')
    zad1('02270812350', datetime.date(2002,7,8), 'm')
    
  except ValueError as ex1:
    print(f'wyjatek klasy ValueError:  {ex1}')
  else:
    print('brak wyjatku')
  try:
    zad3(3)
    
  except ValueError as ex1:
    print(f'wyjatek klasy ValueError:  {ex1}')
  else:
    print('brak wyjatku')
  
  