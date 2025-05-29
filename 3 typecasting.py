# typecasting to zmiana danych na inny typ danych
imie = "Patryk"
wiek = 20
srednia = 4.2
rudy = True
# sprawdzenie typu danych
print(type(imie))
print(type(wiek))
print(type(srednia))
print(type(rudy))
print(".")

# explicit
wiek = float(wiek)
print(type(wiek))

rudy = str(rudy)
print(type(rudy))
print(rudy)

wiek = bool(wiek)
print(wiek) #dla liczb innych od 0 dane stają się True
print(".")

# implicit
x = 2
y = 2.7
x = x*y
print(type(x))
print(x)