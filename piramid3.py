tinggi = int(input ('Masukan tinggi segitiga :'))

for i in range(0, tinggi):
    for j in range (0, tinggi-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print(j+1, end=" ")
    print("\n")
