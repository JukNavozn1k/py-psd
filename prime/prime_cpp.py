import ctypes
from ctypes import c_uint64, c_bool, POINTER, byref, CDLL
from enum import IntEnum
import os

class CppPrimeError(IntEnum):
    OK = 0
    NEGATIVE = 1
    INVALID_INPUT = 2
    TOO_LARGE = 3
    ALLOCATION_FAILED = 4
    NO_SOLUTION = 5

_error_map = {
    CppPrimeError.NEGATIVE: "Negative number",
    CppPrimeError.INVALID_INPUT: "Invalid input",
    CppPrimeError.TOO_LARGE: "Number too large",
    CppPrimeError.ALLOCATION_FAILED: "Memory error",
    CppPrimeError.NO_SOLUTION: "No solution"
}

def _load_lib():
    lib_path = os.path.abspath('./lib/PrimeLib.dll')
    lib = CDLL(lib_path)
    
    # Настройка функций
    lib.is_prime.argtypes = [c_uint64, POINTER(ctypes.c_int)]
    lib.is_prime.restype = c_bool
    
    lib.gcd.argtypes = [c_uint64, c_uint64, POINTER(ctypes.c_int)]
    lib.gcd.restype = c_uint64
    
    lib.lcm.argtypes = [c_uint64, c_uint64, POINTER(ctypes.c_int)]
    lib.lcm.restype = c_uint64
    
    lib.sieve_of_eratosthenes.argtypes = [
        c_uint64, POINTER(c_uint64), POINTER(ctypes.c_int)
    ]
    lib.sieve_of_eratosthenes.restype = POINTER(c_uint64)
    
    lib.goldbach_conjecture.argtypes = [
        c_uint64, POINTER(c_uint64), POINTER(ctypes.c_int)
    ]
    lib.goldbach_conjecture.restype = POINTER(c_uint64)
    
    lib.prime_factors.argtypes = [
        c_uint64, POINTER(c_uint64), POINTER(ctypes.c_int)
    ]
    lib.prime_factors.restype = POINTER(c_uint64)
    
    lib.prime_count.argtypes = [c_uint64, POINTER(ctypes.c_int)]
    lib.prime_count.restype = c_uint64
    
    lib.ferma_test.argtypes = [c_uint64, POINTER(ctypes.c_int)]
    lib.ferma_test.restype = c_bool
    
    lib.free_array.argtypes = [POINTER(c_uint64)]
    lib.free_array.restype = None
    
    return lib

_lib = _load_lib()

def _handle_error(code):
    if code != CppPrimeError.OK:
        err_msg = _error_map.get(CppPrimeError(code), f"Unknown error: {code}")
        raise RuntimeError(err_msg)

def cpp_is_prime(n):
    err = ctypes.c_int(CppPrimeError.OK)
    result = _lib.is_prime(n, byref(err))
    _handle_error(err.value)
    return result

def cpp_gcd(a, b):
    err = ctypes.c_int(CppPrimeError.OK)
    result = _lib.gcd(a, b, byref(err))
    _handle_error(err.value)
    return result

def cpp_lcm(a, b):
    err = ctypes.c_int(CppPrimeError.OK)
    result = _lib.lcm(a, b, byref(err))
    _handle_error(err.value)
    return result

def cpp_sieve(limit):
    count = c_uint64()
    err = ctypes.c_int(CppPrimeError.OK)
    ptr = _lib.sieve_of_eratosthenes(limit, byref(count), byref(err))
    _handle_error(err.value)
    
    try:
        return [ptr[i] for i in range(count.value)]
    finally:
        _lib.free_array(ptr)

def cpp_goldbach(n):
    count = c_uint64()
    err = ctypes.c_int(CppPrimeError.OK)
    ptr = _lib.goldbach_conjecture(n, byref(count), byref(err))
    _handle_error(err.value)
    
    try:
        if count.value != 2:
            raise RuntimeError("Invalid Goldbach pair")
        return (ptr[0], ptr[1])
    finally:
        _lib.free_array(ptr)

def cpp_prime_factors(n):
    count = c_uint64()
    err = ctypes.c_int(CppPrimeError.OK)
    ptr = _lib.prime_factors(n, byref(count), byref(err))
    _handle_error(err.value)
    
    try:
        return [ptr[i] for i in range(count.value)]
    finally:
        _lib.free_array(ptr)

def cpp_prime_count(n):
    err = ctypes.c_int(CppPrimeError.OK)
    result = _lib.prime_count(n, byref(err))
    _handle_error(err.value)
    return result

def cpp_ferma_test(n):
    err = ctypes.c_int(CppPrimeError.OK)
    result = _lib.ferma_test(n, byref(err))
    _handle_error(err.value)
    return result