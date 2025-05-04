
# # MAX_VAL = 2147483647
# MAX_VAL = 18446744073709551615

# class PrimeError(Exception):
#     """Base exception for prime number operations."""
#     pass

# class NegativeNumberError(PrimeError):
#     """Raised when a negative number is provided."""
#     pass

# class InvalidInputError(PrimeError):
#     """Raised when input is invalid for the operation."""
#     pass

# class NumberTooLargeError(PrimeError):
#     """Raised when input number is too large."""
#     pass

# def validate_positive(n: int, operation: str = "operation") -> None:
#     """Validates if number is positive and not too large."""
#     if not isinstance(n, int):
#         raise InvalidInputError(f"Input must be an integer for {operation}")
#     if n < 0:
#         raise NegativeNumberError(f"Number cannot be negative for {operation}")
#     if n > MAX_VAL:  # Новая проверка
#         raise NumberTooLargeError(f"Number cannot be larger than 100 for {operation}")

# def is_prime(n: int) -> bool:
#     """
#     Проверяет, является ли число простым (оптимизированный метод).
    
#     Аргументы:
#         n (int): Число для проверки.
        
#     Возвращает:
#         bool: True, если число простое, иначе False.
#     """
#     validate_positive(n, "primality test")
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     w = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += w
#         w = 6 - w  # Чередование шагов 2 и 4 для пропуска кратных 2 и 3
#     return True


# def prime_factors(n: int) -> list:
#     """
#     Возвращает список простых множителей числа.
    
#     Аргументы:
#         n (int): Число для разложения.
        
#     Возвращает:
#         list: Список простых множителей.
#     """
#     validate_positive(n, "prime factorization")
#     if n == 0:
#         raise InvalidInputError("Cannot factorize zero")
#     factors = []
#     # Обработка делителей 2 и 3
#     for divisor in (2, 3):
#         while n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#     # Обработка остальных делителей (оптимизация через шаги 2 и 4)
#     i = 5
#     w = 2
#     while i * i <= n:
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#         i += w
#         w = 6 - w
#     if n > 1:
#         factors.append(n)
#     return factors


# def gcd(a: int, b: int) -> int:
#     """
#     Вычисляет НОД двух чисел с помощью алгоритма Евклида.
    
#     Аргументы:
#         a, b (int): Числа для вычисления.
        
#     Возвращает:
#         int: Наибольший общий делитель.
#     """
#     validate_positive(a, "GCD")
#     validate_positive(b, "GCD")
#     if a == 0 and b == 0:
#         raise InvalidInputError("GCD is undefined for (0,0)")
#     while b:
#         a, b = b, a % b
#     return a


# def lcm(a: int, b: int) -> int:
#     """
#     Вычисляет НОК двух чисел через НОД.
    
#     Аргументы:
#         a, b (int): Числа для вычисления.
        
#     Возвращает:
#         int: Наименьшее общее кратное.
#     """
#     validate_positive(a, "LCM")
#     validate_positive(b, "LCM")
#     if a == 0 or b == 0:
#         raise InvalidInputError("LCM is undefined for zero")
#     return a * b // gcd(a, b)


# def sieve_of_eratosthenes(limit: int) -> list:
#     """
#     Генерирует список простых чисел до заданного предела (оптимизированное решето).
    
#     Аргументы:
#         limit (int): Верхняя граница поиска.
        
#     Возвращает:
#         list: Список простых чисел.
#     """
#     validate_positive(limit, "sieve of Eratosthenes")
#     if limit < 2:
#         return []
#     sieve = [True] * (limit + 1)
#     sieve[0], sieve[1] = False, False
#     # Начинаем с 2, оптимизация отметки кратных
#     for num in range(2, int(limit**0.5) + 1):
#         if sieve[num]:
#             sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
#     return [num for num, is_prime in enumerate(sieve) if is_prime]


# def goldbach_conjecture(n: int) -> list:
#     """
#     Проверяет гипотезу Гольдбаха: возвращает два простых числа, сумма которых равна n.
    
#     Аргументы:
#         n (int): Четное число > 2.
        
#     Возвращает:
#         list: Пара простых чисел или пустой список, если гипотеза не выполняется.
#     """
#     validate_positive(n, "Goldbach conjecture")
#     if n <= 2:
#         raise InvalidInputError("Number must be greater than 2 for Goldbach conjecture")
#     if n % 2 != 0:
#         raise InvalidInputError("Number must be even for Goldbach conjecture")
#     primes = sieve_of_eratosthenes(n)
#     prime_set = set(primes)  # Для быстрой проверки наличия элемента
#     for p in primes:
#         if p > n // 2:
#             break
#         if (n - p) in prime_set:
#             return [p, n - p]
#     return []


MAX_VAL = 18446744073709551615

class PrimeError(Exception): pass
class NegativeNumberError(PrimeError): pass
class InvalidInputError(PrimeError): pass
class NumberTooLargeError(PrimeError): pass


# Вспомогательная функция для вызова исключений в лямбдах
_raise = lambda ex: [exec(f'raise {ex.__class__.__name__}(f"""{ex}""")')]

# Лямбда-версия validate_positive
validate_positive = lambda n, op="operation": (
    (isinstance(n, int) or _raise(InvalidInputError(f"Input must be integer for {op}"))[0]) and
    (n >= 0 or _raise(NegativeNumberError(f"Number cannot be negative for {op}"))[0]) and
    (n <= MAX_VAL or _raise(NumberTooLargeError(f"Number ≤ {MAX_VAL} required for {op}"))[0])
)

# Лямбда-функции
is_prime = lambda n: (validate_positive(n, "primality test"), n > 1 and (n in (2,3) or (n%2 != 0 and n%3 != 0 and all(n%i != 0 and n%(i+2)!=0 for i in range(5, int(n**0.5)+1, 6)))))[1]

gcd = lambda a, b: (validate_positive(a, "GCD"), validate_positive(b, "GCD"), (lambda: a if b == 0 else gcd(b, a % b))())[2]

lcm = lambda a, b: (validate_positive(a, "LCM"), validate_positive(b, "LCM"), (a * b) // gcd(a, b))[2]

sieve_of_eratosthenes = lambda limit: (validate_positive(limit, "sieve"), [i for i in ([] if limit < 2 else range(2, limit+1)) if all(i % d for d in range(2, int(i**0.5)+1))])[1]

goldbach_conjecture = lambda n: (
    validate_positive(n, "Goldbach"),
    next(([p, n-p] for p in sieve_of_eratosthenes(n) if is_prime(n-p)), [])
)[1] if (n%2 == 0 and n > 2) else _raise(InvalidInputError("Number must be even and > 2"))


def prime_factors(n: int) -> list:
    validate_positive(n, "prime factorization")
    if n == 0: raise InvalidInputError("Cannot factorize zero")
    
    factors = []
    for divisor in (2, 3):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    i, w = 5, 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += w
        w = 6 - w
    if n > 1: factors.append(n)
    return factors

prime_count = lambda n: len(validate_positive(n, 'prime count'), sieve_of_eratosthenes(n))
ferma_test = lambda n: (validate_positive(n, 'ferma test'),n > 1 and all(pow(a, n-1, n) == 1 for a in (2, 3, 5, 7)))[-1]