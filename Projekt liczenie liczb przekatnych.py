# Otrzymujemy liczbe boków wielokąta
n = float(input("Ile boków ma wielokąt:"))
n = int(n)   #ustawiamy pełny wynik, bo wielokąt nie może miec niepelnej ilosci boków
 # Liczymy liczbę przekątnych
odp = float(n*(n-3)/2)
# Zwracamy wynik   #round() służy do zaokrąglania
print(f"{n}-kąt ma {round(odp, 2)} przekątnych")