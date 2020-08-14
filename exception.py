try:
    a = '1'
    b = '0'
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
try:
    c = '2'
    d = '$'
    print(int(c)/int(d))
except ValueError:
    print("Error Code: invalid literal for int() with base 10: '$'")
try: 
    e = '3'
    f = '1'
    print(int(int(e)/int(f)))
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")