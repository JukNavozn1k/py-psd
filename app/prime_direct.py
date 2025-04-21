from .prime_interface import PrimeCalculator
from .prime import (
    is_prime as _is_prime,
    prime_factors as _prime_factors,
    gcd as _gcd,
    lcm as _lcm,
    sieve_of_eratosthenes as _sieve,
    goldbach_conjecture as _goldbach
)

class DirectPrimeCalculator(PrimeCalculator):
    def is_prime(self, n: int) -> bool:
        return _is_prime(n)
    
    def prime_factors(self, n: int) -> list[int]:
        return _prime_factors(n)
    
    def gcd(self, a: int, b: int) -> int:
        return _gcd(a, b)
    
    def lcm(self, a: int, b: int) -> int:
        return _lcm(a, b)
    
    def sieve(self, limit: int) -> list[int]:
        return _sieve(limit)
    
    def goldbach(self, n: int) -> list[int]:
        return _goldbach(n)
