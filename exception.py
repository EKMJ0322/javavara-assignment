for i in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as err:
        print("Error Code:", err)