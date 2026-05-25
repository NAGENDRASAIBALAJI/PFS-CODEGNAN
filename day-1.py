rows = 10

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("20" '-')

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print() 
