n = int(input())
j= 1

for i in range(n):
    for j in range(j, j+3):
        print(f"{j}", end=" ")
    j = j + 2
    print("PUM")