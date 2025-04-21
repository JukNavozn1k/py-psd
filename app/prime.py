def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым (оптимизированный метод).
    
    Аргументы:
        n (int): Число для проверки.
        
    Возвращает:
        bool: True, если число простое, иначе False.
    """
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
    return a * b // gcd(a, b)


def sieve_of_eratosthenes(limit: int) -> list:
    """
    Генерирует список простых чисел до заданного предела (оптимизированное решето).
    
    Аргументы:
        limit (int): Верхняя граница поиска.
        
    Возвращает:
        list: Список простых чисел.
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    # Начинаем с 2, оптимизация отметки кратных
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
    return [num for num, is_prime in enumerate(sieve) if is_prime]


# def goldbach_conjecture(n: int) -> list:
#     """
#     Проверяет гипотезу Гольдбаха: возвращает два простых числа, сумма которых равна n.
    
#     Аргументы:
#         n (int): Четное число > 2.
        
#     Возвращает:
#         list: Пара простых чисел или пустой список, если гипотеза не выполняется.
#     """
#     if n <= 2 or n % 2 != 0:
#         return []
#     primes = sieve_of_eratosthenes(n)
#     prime_set = set(primes)  # Для быстрой проверки наличия элемента
#     for p in primes:
#         if p > n // 2:
#             break
#         if (n - p) in prime_set:
#             return [p, n - p]
#     return []


