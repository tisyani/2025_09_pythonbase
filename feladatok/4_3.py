"""1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,
majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!"""

import random
random_number = random.randint(1,3)
guess_number = int(input("Adj meg egy számot 1 és 3 között: "))

if random_number == guess_number:
    print ("eltalaltad ocsipok")
else:
    print(f"az bebaszna, {random_number}: ez volt a helyes")
