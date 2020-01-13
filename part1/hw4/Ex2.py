n = int(input("Посчитать сумму чисел фибоначxи до n = ?: "))


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibo_sum(n):
    result = [fibonacci(i) for i in range(1, n+1)]
    print(result)
    return sum(result)


print('Cумму чисел фибоначxи до n =', n,':', fibo_sum(n))
