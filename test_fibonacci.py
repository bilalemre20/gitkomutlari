import unittest

# Fibonacci fonksiyonu
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_dizisi = [0, 1]
        for _ in range(2, n):
            fib_dizisi.append(fib_dizisi[-1] + fib_dizisi[-2])
        return fib_dizisi

class TestFibonacci(unittest.TestCase):
    def test_negative_input(self):
        """Negatif girişler boş liste döndürmeli."""
        self.assertEqual(fibonacci(-5), [])
        self.assertEqual(fibonacci(0), [])

    def test_small_inputs(self):
        """Küçük pozitif girişler doğru liste döndürmeli."""
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])

    def test_normal_sequence(self):
        """Normal Fibonacci serisi doğru hesaplanmalı."""
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_reversed_sequence(self):
        """Ters çevrilmiş Fibonacci serisi doğru hesaplanmalı."""
        fib_dizisi = fibonacci(6)
        reversed_sequence = fib_dizisi[::-1]
        self.assertEqual(reversed_sequence, [5, 3, 2, 1, 1, 0])

    def test_large_sequence(self):
        """Büyük Fibonacci serileri doğru hesaplanmalı."""
        fib_dizisi = fibonacci(20)
        self.assertEqual(len(fib_dizisi), 20)
        self.assertEqual(fib_dizisi[19], 4181)  # 20. eleman (0'dan başladığı için)

if __name__ == "__main__":
    unittest.main()
