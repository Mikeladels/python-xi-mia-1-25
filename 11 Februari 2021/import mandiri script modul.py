#michelle adelia suwarno / xi mia 1 / 25
#import madiri script modul

def fib(n) : #write fibonacci series up to n
    a, b = 0, 1
    while a < n :
        print(a, end='')
        a, b = b, a+b
    print()

def fib2(n) : #return fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n :
        result.append (a)
        a, b = b, a+b
    return result