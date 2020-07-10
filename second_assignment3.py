a = input()
b, c = input().split()
b = int (b)
a_length = len(a)
if len(a)>=b:
    print(a.replace(a[b], c))
else:
    print("The number you gave is too large!")
