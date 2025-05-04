import ctypes
from ctypes import c_uint64, c_bool, c_size_t, c_char_p, POINTER, byref
import os

# Загрузка DLL
dll_path = os.path.abspath('./lib/PrimeLib.dll')
prime_lib = ctypes.CDLL(dll_path)

# Объявление типов и функций
prime_lib.is_prime.argtypes = [c_uint64, POINTER(c_bool), POINTER(c_char_p)]
prime_lib.is_prime.restype = c_bool

prime_lib.gcd.argtypes = [c_uint64, c_uint64, POINTER(c_uint64), POINTER(c_char_p)]
prime_lib.gcd.restype = c_bool

prime_lib.lcm.argtypes = [c_uint64, c_uint64, POINTER(c_uint64), POINTER(c_char_p)]
prime_lib.lcm.restype = c_bool

prime_lib.sieve_of_eratosthenes.argtypes = [
    c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_size_t), POINTER(c_char_p)
]
prime_lib.sieve_of_eratosthenes.restype = c_bool

prime_lib.goldbach_conjecture.argtypes = [
    c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_size_t), POINTER(c_char_p)
]
prime_lib.goldbach_conjecture.restype = c_bool

prime_lib.prime_factors.argtypes = [
    c_uint64, POINTER(POINTER(c_uint64)), POINTER(c_size_t), POINTER(c_char_p)
]
prime_lib.prime_factors.restype = c_bool

prime_lib.prime_count.argtypes = [c_uint64, POINTER(c_uint64), POINTER(c_char_p)]
prime_lib.prime_count.restype = c_bool

prime_lib.ferma_test.argtypes = [c_uint64, POINTER(c_bool), POINTER(c_char_p)]
prime_lib.ferma_test.restype = c_bool

prime_lib.free_array.argtypes = [POINTER(c_uint64)]
prime_lib.free_array.restype = None

class PrimeError(Exception):
    pass

def handle_error(error_msg):
    if error_msg:
        raise PrimeError(error_msg.decode('utf-8'))
    raise PrimeError("Unknown error")

# Обертки для функций
def is_prime(n):
    result = c_bool()
    error_msg = c_char_p()
    success = prime_lib.is_prime(n, byref(result), byref(error_msg))
    if not success:
        handle_error(error_msg.value)
    return result.value

def gcd(a, b):
    result = c_uint64()
    error_msg = c_char_p()
    success = prime_lib.gcd(a, b, byref(result), byref(error_msg))
    if not success:
        handle_error(error_msg.value)
    return result.value

def lcm(a, b):
    result = c_uint64()
    error_msg = c_char_p()
    success = prime_lib.lcm(a, b, byref(result), byref(error_msg))
    if not success:
        handle_error(error_msg.value)
    return result.value

def sieve_of_eratosthenes(limit):
    primes_ptr = POINTER(c_uint64)()
    count = c_size_t()
    error_msg = c_char_p()
    
    success = prime_lib.sieve_of_eratosthenes(
        limit, byref(primes_ptr), byref(count), byref(error_msg))
    
    if not success:
        handle_error(error_msg.value)
    
    try:
        return [primes_ptr[i] for i in range(count.value)]
    finally:
        prime_lib.free_array(primes_ptr)

def goldbach_conjecture(n):
    pair_ptr = POINTER(c_uint64)()
    count = c_size_t()
    error_msg = c_char_p()
    
    success = prime_lib.goldbach_conjecture(
        n, byref(pair_ptr), byref(count), byref(error_msg))
    
    if not success:
        handle_error(error_msg.value)
    
    try:
        if count.value != 2:
            raise PrimeError("Unexpected number of elements in Goldbach pair")
        return (pair_ptr[0], pair_ptr[1])
    finally:
        prime_lib.free_array(pair_ptr)

def prime_factors(n):
    factors_ptr = POINTER(c_uint64)()
    count = c_size_t()
    error_msg = c_char_p()
    
    success = prime_lib.prime_factors(
        n, byref(factors_ptr), byref(count), byref(error_msg))
    
    if not success:
        handle_error(error_msg.value)
    
    try:
        return [factors_ptr[i] for i in range(count.value)]
    finally:
        prime_lib.free_array(factors_ptr)

def prime_count(n):
    result = c_uint64()
    error_msg = c_char_p()
    success = prime_lib.prime_count(n, byref(result), byref(error_msg))
    if not success:
        handle_error(error_msg.value)
    return result.value

def ferma_test(n):
    result = c_bool()
    error_msg = c_char_p()
    success = prime_lib.ferma_test(n, byref(result), byref(error_msg))
    if not success:
        handle_error(error_msg.value)
    return result.value

# Примеры использования
if __name__ == "__main__":
    try:
        print("Is 17 prime?", is_prime(17))
        print("GCD(48, 18):", gcd(48, 18))
        print("LCM(4, 6):", lcm(4, 6))
        print("Primes up to 30:", sieve_of_eratosthenes(30))
        print("Goldbach pair for 28:", goldbach_conjecture(28))
        print("Prime factors of 100:", prime_factors(100))
        print("Number of primes <= 30:", prime_count(30))
        print("Fermat test for 17:", ferma_test(17))
        
        # Тест ошибок
        # print(gcd(0, 0))  # Вызовет исключение
    except PrimeError as e:
        print(f"Error: {e}")