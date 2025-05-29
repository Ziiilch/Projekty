import math
# funkcje matematyczne
a = 3.14
b = -5
c = 9

# przybliżenie
x = round(a)
print(x)

# wart. bezwzgl
y = abs(b)
print(y)

# potęga
z = pow(c,2)
print(z)

# wartosc maksymalna zbioru
d = max(a,b,c)
e = min(a,b,c)
print(d)
print(e)

# działają tylko jeśli zapisze się "import math"

# pi
print(math.pi)

# euler
print(math.e)

# pierwiastek
print(math.sqrt(c))

# zaokrąglenia
# góra
print(math.ceil(a))
# dół
print(math.floor(a))