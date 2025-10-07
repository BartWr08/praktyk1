import math
import time
liczba = int(input('wpisz liczbe do sprawdznia: '))
start = time.time()
liczba_pierwsza = True
for dzielnik in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % dzielnik == 0:
            liczba_pierwsza = False
if liczba_pierwsza:
    print('podana liczba jest liczbom pierwszom')
else:
    print('podana liczba nie jest liczbom pierwszom')
print('czas obliczen ',time.time() - start)