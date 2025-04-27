class PrimeError(Exception):
    """Base exception for prime number operations."""
    pass

class NegativeNumberError(PrimeError):
    """Raised when a negative number is provided."""
    pass

class InvalidInputError(PrimeError):
    """Raised when input is invalid for the operation."""
    pass

def validate_positive(n: int, operation: str = "operation") -> None:
    """Validates if number is positive."""
    if not isinstance(n, int):
        raise InvalidInputError(f"Input must be an integer for {operation}")
    if n < 0:
        raise NegativeNumberError(f"Number cannot be negative for {operation}")

def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым (оптимизированный метод).
    
    Аргументы:
        n (int): Число для проверки.
        
    Возвращает:
        bool: True, если число простое, иначе False.
    """
    validate_positive(n, "primality test")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # Чередование шагов 2 и 4 для пропуска кратных 2 и 3
    return True


def prime_factors(n: int) -> list:
    """
    Возвращает список простых множителей числа.
    
    Аргументы:
        n (int): Число для разложения.
        
    Возвращает:
        list: Список простых множителей.
    """
    validate_positive(n, "prime factorization")
    if n == 0:
        raise InvalidInputError("Cannot factorize zero")
    factors = []
    # Обработка делителей 2 и 3
    for divisor in (2, 3):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    # Обработка остальных делителей (оптимизация через шаги 2 и 4)
    i = 5
    w = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += w
        w = 6 - w
    if n > 1:
        factors.append(n)
    return factors


def gcd(a: int, b: int) -> int:
    """
    Вычисляет НОД двух чисел с помощью алгоритма Евклида.
    
    Аргументы:
        a, b (int): Числа для вычисления.
        
    Возвращает:
        int: Наибольший общий делитель.
    """
    validate_positive(a, "GCD")
    validate_positive(b, "GCD")
    if a == 0 and b == 0:
        raise InvalidInputError("GCD is undefined for (0,0)")
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Вычисляет НОК двух чисел через НОД.
    
    Аргументы:
        a, b (int): Числа для вычисления.
        
    Возвращает:
        int: Наименьшее общее кратное.
    """
    validate_positive(a, "LCM")
    validate_positive(b, "LCM")
    if a == 0 or b == 0:
        raise InvalidInputError("LCM is undefined for zero")
    return a * b // gcd(a, b)


def sieve_of_eratosthenes(limit: int) -> list:
    """
    Генерирует список простых чисел до заданного предела (оптимизированное решето).
    
    Аргументы:
        limit (int): Верхняя граница поиска.
        
    Возвращает:
        list: Список простых чисел.
    """
    validate_positive(limit, "sieve of Eratosthenes")
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    # Начинаем с 2, оптимизация отметки кратных
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def goldbach_conjecture(n: int) -> list:
    """
    Проверяет гипотезу Гольдбаха: возвращает два простых числа, сумма которых равна n.
    
    Аргументы:
        n (int): Четное число > 2.
        
    Возвращает:
        list: Пара простых чисел или пустой список, если гипотеза не выполняется.
    """
    validate_positive(n, "Goldbach conjecture")
    if n <= 2:
        raise InvalidInputError("Number must be greater than 2 for Goldbach conjecture")
    if n % 2 != 0:
        raise InvalidInputError("Number must be even for Goldbach conjecture")
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)  # Для быстрой проверки наличия элемента
    for p in primes:
        if p > n // 2:
            break
        if (n - p) in prime_set:
            return [p, n - p]
    return []


