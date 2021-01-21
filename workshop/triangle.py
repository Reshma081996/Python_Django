n=int(input("enter num of rows:"))
for i in range(0,n+1):
    if (i == n):
        print("*"*((2*n)+1))

    elif (i==0):
        print(" "*(n-i)+"*"*1)
    else:
        print(" " * (n - i) + "*" * 1 + " " * (2 * (i-1) + 1) + "*" * 1)

print()
