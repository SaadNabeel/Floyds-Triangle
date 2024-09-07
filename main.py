n=int(input("Enter a number of rows: "))
a=0
for c in range(n+1):
    for d in range(c):
        a=a+1
        print(a, end=" ")
    print()