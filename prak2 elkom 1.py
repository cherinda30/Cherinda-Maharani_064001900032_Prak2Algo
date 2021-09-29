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

formula = input('sisi mana yang akan dihitung? (a,b,c) ')

if formula == 'c':

    
	side_a = int(input('masukkan panjang a: '))
	side_b = int(input('masukkan panjang b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('panjang c adalah: ' )
	print(side_c)

elif formula == 'a':
    side_b = int(input('masukkan panjang b: '))
    side_c = int(input('masukkan panjang c: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print('panjang a adalah' )
    print(side_a)

elif formula == 'b':
    side_a = int(input('masukkan panjang a: '))
    side_c = int(input('masukkan panjang c: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print('panjnag b adalah')
    print(side_c)

else:
	print('tolong pilih antara a,b atau c')
	