"""2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

fej = 1
iras = 2

import random
random_szam = random.randint(1,2)

valasz = (input("Fej vagy írás?: "))

if valasz == fej and random_szam == 1:
    print("helyes")
elif valasz == iras and random_szam == 2:
    print("helyes")
else:
    print("helytelen")