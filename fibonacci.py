def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_dizisi = [0, 1]
        for i in range(2, n):
            fib_dizisi.append(fib_dizisi[-1] + fib_dizisi[-2])
        return fib_dizisi

if __name__ == "__main__":
    try:
        n = int(input("Fibonacci serisinin eleman sayısını girin: "))
        print(fibonacci(n))
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin!")