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
  int(input('Masukkan angka pertama: ')),
  int(input('Masukkan angka kedua: ')),
  int(input('Masukkan angka ketiga: '))
)

if a > b and a > c:
  print('Angka terbesar adalah angka pertama: ', a)
elif b > a and b > c:
  print('Angka terbesar adalah angka kedua: ', b)
else:
  print('Angka terbesar adalah angka ketiga: ', c)
