import ctypes
from ctypes import c_int64, c_bool, Structure, POINTER, CFUNCTYPE
from enum import IntEnum
import os

# Загрузка DLL
dll_path = os.path.abspath('PrimeLib.dll')  
prime_lib = ctypes.CDLL(dll_path)

class PrimeErrorCode(IntEnum):
    PRIME_NO_ERROR = 0
    PRIME_NEGATIVE_NUMBER_ERROR = 1
    PRIME_INVALID_INPUT_ERROR = 2
    PRIME_NUMBER_TOO_LARGE_ERROR = 3
    PRIME_UNDEFINED_ERROR = 4
    PRIME_INVALID_INPUT_ZERO_ERROR = 5
    PRIME_GOLDBACH_INVALID_INPUT_ERROR = 6

class PrimeIntArray(Structure):
    _fields_ = [
        ('data', POINTER(c_int64)),
        ('length', ctypes.c_int)
    ]

# Объявление функций
prime_lib.IsPrime.argtypes = [c_int64, ctypes.POINTER(c_bool)]
prime_lib.IsPrime.restype = ctypes.c_int

prime_lib.PrimeFactors.argtypes = [c_int64, ctypes.POINTER(PrimeIntArray)]
prime_lib.PrimeFactors.restype = ctypes.c_int

prime_lib.GCD.argtypes = [c_int64, c_int64, ctypes.POINTER(c_int64)]
prime_lib.GCD.restype = ctypes.c_int

prime_lib.LCM.argtypes = [c_int64, c_int64, ctypes.POINTER(c_int64)]
prime_lib.LCM.restype = ctypes.c_int

prime_lib.SieveOfEratosthenes.argtypes = [c_int64, ctypes.POINTER(PrimeIntArray)]
prime_lib.SieveOfEratosthenes.restype = ctypes.c_int

prime_lib.GoldbachConjecture.argtypes = [c_int64, ctypes.POINTER(PrimeIntArray)]
prime_lib.GoldbachConjecture.restype = ctypes.c_int

prime_lib.FreePrimeIntArray.argtypes = [ctypes.POINTER(PrimeIntArray)]
prime_lib.FreePrimeIntArray.restype = None

class PrimeError(Exception):
    pass

def check_error(result, func, args):
    if result != PrimeErrorCode.PRIME_NO_ERROR:
        raise PrimeError(PrimeErrorCode(result).name)
    return result

# Декоратор для обработки ошибок
def handle_errors(func):
    def wrapper(*args):
        error_code = func(*args)
        if error_code != PrimeErrorCode.PRIME_NO_ERROR:
            raise PrimeError(PrimeErrorCode(error_code).name)
    return wrapper

# Обертки для функций
def is_prime(n):
    result = c_bool()
    error_code = prime_lib.IsPrime(n, ctypes.byref(result))
    if error_code != PrimeErrorCode.PRIME_NO_ERROR:
        raise PrimeError(PrimeErrorCode(error_code).name)
    return result.value

def prime_factors(n):
    arr = PrimeIntArray()
    error_code = prime_lib.PrimeFactors(n, ctypes.byref(arr))
    try:
        if error_code != PrimeErrorCode.PRIME_NO_ERROR:
            raise PrimeError(PrimeErrorCode(error_code).name)
        return [arr.data[i] for i in range(arr.length)]
    finally:
        prime_lib.FreePrimeIntArray(ctypes.byref(arr))

def gcd(a, b):
    result = c_int64()
    error_code = prime_lib.GCD(a, b, ctypes.byref(result))
    if error_code != PrimeErrorCode.PRIME_NO_ERROR:
        raise PrimeError(PrimeErrorCode(error_code).name)
    return result.value

def lcm(a, b):
    result = c_int64()
    error_code = prime_lib.LCM(a, b, ctypes.byref(result))
    if error_code != PrimeErrorCode.PRIME_NO_ERROR:
        raise PrimeError(PrimeErrorCode(error_code).name)
    return result.value

def sieve_of_eratosthenes(limit):
    arr = PrimeIntArray()
    error_code = prime_lib.SieveOfEratosthenes(limit, ctypes.byref(arr))
    try:
        if error_code != PrimeErrorCode.PRIME_NO_ERROR:
            raise PrimeError(PrimeErrorCode(error_code).name)
        return [arr.data[i] for i in range(arr.length)]
    finally:
        prime_lib.FreePrimeIntArray(ctypes.byref(arr))

def goldbach_conjecture(n):
    arr = PrimeIntArray()
    error_code = prime_lib.GoldbachConjecture(n, ctypes.byref(arr))
    try:
        if error_code != PrimeErrorCode.PRIME_NO_ERROR:
            raise PrimeError(PrimeErrorCode(error_code).name)
        return (arr.data[0], arr.data[1])
    finally:
        prime_lib.FreePrimeIntArray(ctypes.byref(arr))

# Примеры использования
if __name__ == "__main__":
    try:
        print("Is 17 prime?", is_prime(17))
        print("Prime factors of 100:", prime_factors(100))
        print("GCD(48, 18):", gcd(48, 18))
        print("LCM(4, 6):", lcm(4, 6))
        print("Primes up to 30:", sieve_of_eratosthenes(30))
        print("Goldbach pair for 28:", goldbach_conjecture(28))
        
        # Тест ошибок
        # print(is_prime(-5))  # Вызовет исключение
    except PrimeError as e:
        print(f"Error: {e}")