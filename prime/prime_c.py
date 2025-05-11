# prime_c.py
from ctypes import *
import sys
import platform

class CPrimeError(Exception):
    pass

# Загрузка библиотеки
if platform.system() == 'Windows':
    lib = CDLL('./lib/PrimeLib.dll')

# Определение типов
lib.is_prime.argtypes = [c_uint64, POINTER(c_bool)]
lib.is_prime.restype = c_int
lib.gcd.argtypes = [c_uint64, c_uint64, POINTER(c_uint64)]
lib.gcd.restype = c_int
lib.lcm.argtypes = [c_uint64, c_uint64, POINTER(c_uint64)]
lib.lcm.restype = c_int
lib.sieve_of_eratosthenes.argtypes = [c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_uint64)]
lib.sieve_of_eratosthenes.restype = c_int
lib.goldbach_conjecture.argtypes = [c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_uint64)]
lib.goldbach_conjecture.restype = c_int
lib.prime_factors.argtypes = [c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_uint64)]
lib.prime_factors.restype = c_int
lib.prime_count.argtypes = [c_uint64, POINTER(c_uint64)]
lib.prime_count.restype = c_int
lib.ferma_test.argtypes = [c_uint64, POINTER(c_bool)]
lib.ferma_test.restype = c_int
lib.free_array.argtypes = [POINTER(c_uint64)]
lib.free_array.restype = None

# Error mapping
ERROR_MAPPING = {
    0: None,  # PRIME_OK
    1: CPrimeError("Number cannot be negative"),
    2: CPrimeError("Invalid input"),
    3: CPrimeError("Number too large"),
    4: CPrimeError("Zero is invalid input")
}

def _check_error(err_code):
    if err_code != 0:
        error = ERROR_MAPPING.get(err_code, CPrimeError(f"Unknown error code: {err_code}"))
        raise error

# Обёртки функций
def c_is_prime(n: int) -> bool:
    result = c_bool()
    err = lib.is_prime(c_uint64(n), byref(result))
    _check_error(err)
    return result.value

def c_gcd(a: int, b: int) -> int:
    result = c_uint64()
    err = lib.gcd(c_uint64(a), c_uint64(b), byref(result))
    _check_error(err)
    return result.value

def c_lcm(a: int, b: int) -> int:
    result = c_uint64()
    err = lib.lcm(c_uint64(a), c_uint64(b), byref(result))
    _check_error(err)
    return result.value

def c_sieve(limit: int) -> list:
    primes_ptr = POINTER(c_uint64)()
    count = c_uint64()
    err = lib.sieve_of_eratosthenes(c_uint64(limit), byref(primes_ptr), byref(count))
    _check_error(err)
    
    primes = [primes_ptr[i] for i in range(count.value)]
    lib.free_array(primes_ptr)
    return primes

def c_goldbach(n: int) -> list:
    result_ptr = POINTER(c_uint64)()
    size = c_uint64()
    err = lib.goldbach_conjecture(c_uint64(n), byref(result_ptr), byref(size))
    
    if err != 0:
        if err == 2:
            raise CPrimeError("Goldbach conjecture requires even number > 2")
        _check_error(err)
    
    result = [result_ptr[i] for i in range(size.value)]
    lib.free_array(result_ptr)
    return result

def c_prime_factors(n: int) -> list:
    factors_ptr = POINTER(c_uint64)()
    count = c_uint64()
    err = lib.prime_factors(c_uint64(n), byref(factors_ptr), byref(count))
    _check_error(err)
    
    factors = [factors_ptr[i] for i in range(count.value)]
    lib.free_array(factors_ptr)
    return factors

def c_prime_count(n: int) -> int:
    count = c_uint64()
    err = lib.prime_count(c_uint64(n), byref(count))
    _check_error(err)
    return count.value

def c_ferma_test(n: int) -> bool:
    result = c_bool()
    err = lib.ferma_test(c_uint64(n), byref(result))
    _check_error(err)
    return result.value

