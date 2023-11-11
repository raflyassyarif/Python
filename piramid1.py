no = int (input ('Masukan angka :'))
for x in range (0,no):
    for y in range (0, no-x-1):
        print (end=' ')
    for y in range (0, x+1):
        print ('*', end=' ')
    print()