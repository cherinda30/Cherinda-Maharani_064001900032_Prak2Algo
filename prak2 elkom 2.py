#AlgoPrak2_Cherinda Maharani

print ("           /$$                           /$$                 /$$          ")
print ("          | $$                          |__/                | $$          ")
print ("  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$$$$$$   /$$$$$$$  /$$$$$$ ")
print (" /$$_____/| $$__  $$ /$$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$ |____  $$")
print ("| $$      | $$  \ $$| $$$$$$$$| $$  \__/| $$| $$  \ $$| $$  | $$  /$$$$$$$")
print ("| $$      | $$  | $$| $$_____/| $$      | $$| $$  | $$| $$  | $$ /$$__  $$")
print ("|  $$$$$$$| $$  | $$|  $$$$$$$| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$")
print (" \_______/|__/  |__/ \_______/|__/      |__/|__/  |__/ \_______/ \_______/")

from math import sqrt

a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if a > b and a > c:
  print('A yang terbesar', a)
elif b > a and b > c:
  print('B yang terbesar', b)
else:
  print('C yang terbesar', c)