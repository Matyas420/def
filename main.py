def soucet(cislo1, cislo2):
  return cislo1 + cislo2


def rozdil(cislo1, cislo2):
  return cislo1 - cislo2

def soucin(cislo1, cislo2):
  return cislo1 * cislo2

def podíl(cislo1, cislo2):
  return cislo1 / cislo2

def mocnina(cislo1, cislo2):
  return cislo1 ** cislo2

def odmocnina(cislo1, cislo2):
  return cislo1 // cislo2
  
while True:
  print("Vítej v kalkulačce")
  cislo1 = float(input("Zadej číslo: "))
  cislo2 = float(input("Zadej číslo: "))
  operace = input("Zadej operaci: ")
  if operace == "+":
    print(soucet(cislo1, cislo2))
  elif operace == "-":
    print(rozdil(cislo1, cislo2))
  elif operace == "*":
    print(soucin(cislo1, cislo2))
  elif cislo2 == 0 and operace == "/":
    print("Nulou nelze dělit")
  elif operace == "/":
    print(podíl(cislo1, cislo2))
  elif operace == "**":
    print(mocnina(cislo1, cislo2))
  elif operace == "//":
    print(odmocnina(cislo1, cislo2))
  else: 
    print("zadana hodnota je nespravna")
  pokracovat = input("Chcete pokracovat? (a/n): ")
  if pokracovat == 'n': 
    print("Děkujeme za použití kalkulačky") 
    break

