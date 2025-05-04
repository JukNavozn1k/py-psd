from .prime import (
    is_prime as py_is_prime,
    prime_factors as py_prime_factors,
    gcd as py_gcd,
    lcm as py_lcm,
    sieve_of_eratosthenes as py_sieve,
    goldbach_conjecture as py_goldbach,
    PrimeError,
    NegativeNumberError,
    InvalidInputError,
    NumberTooLargeError,
    validate_positive,
    ferma_test as py_ferma_test
)

from .prime_cpp import (
    is_prime as cpp_is_prime,
    prime_factors as cpp_prime_factors,
    gcd as cpp_gcd,
    lcm as cpp_lcm,
    sieve_of_eratosthenes as cpp_sieve,
    goldbach_conjecture as cpp_goldbach,
    PrimeError as CppPrimeError,
    ferma_test as cpp_ferma_test
)

# Default implementations 
is_prime = py_is_prime
prime_factors = py_prime_factors
gcd = py_gcd
lcm = py_lcm
sieve_of_eratosthenes = py_sieve
goldbach_conjecture = py_goldbach
ferma_test = py_ferma_test