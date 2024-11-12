from Duona import Duona
from Kepykla import Kepykla

duona1 = Duona ("Kvietinė", 120, 1.20, 450)
print(duona1)
duona2 = Duona ("Rūginė", 125, 1.45, 430)
print(duona2)
duona3 = Duona ("Pilno grūdo", 100, 1.10, 410)
print(duona3)

brangiausia_duona = max([duona1, duona2, duona3], key = lambda x: x.Price)
print(f' Brangiausia: {brangiausia_duona}')

lengviausia_duona = min([duona1, duona2, duona3], key = lambda x: x.Weight)
print(f' Lengviausia: {lengviausia_duona}')


Pamaina1 = Kepykla ("Klaipėdos mažoji", 100, 125, 75, 500)

kvietinė_plotas = duona1.shelfSquare(Pamaina1.Quantity_kvietinė)
rūginė_plotas = duona2.shelfSquare(Pamaina1.Quantity_rūginė)
pilno_grudo_plotas = duona3.shelfSquare(Pamaina1.Quantity_pilno_grūdo)

print(f'Kvietinei duonai reikalingas plotas {kvietinė_plotas} kv.m')
print(f'Rūginei duonai reikalingas plotas {rūginė_plotas} kv.m')
print(f'Pilno grūdo duonai reikalingas plotas {pilno_grudo_plotas} kv.m')

print(f'Reikės atlikti {Pamaina1.totalWeight(duona1, duona2, duona3)} pervežimus')
