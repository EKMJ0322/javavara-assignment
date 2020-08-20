cube = lambda x: x**3 

def fibonacci(n):
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i-2]+a[i-1])
    return a

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))