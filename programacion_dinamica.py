def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    print (n)
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n,memo={}):
    """
    Fibonacci con memoria
    """
    if n==0 or n==1:
        return 1
    try:
        memo[n]
    except KeyError:
        resultado= fibonacci_dinamico(n-1,memo) + fibonacci_dinamico(n-2,memo)
        memo[n]=resultado
        return resultado        


if __name__ == "__main__":
    n=int(input("Elige que numero de fibonacci quieres "))
    fibonnacci=fibonacci_dinamico(n)
    print(fibonnacci)
    