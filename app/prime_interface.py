from abc import ABC, abstractmethod
from typing import List, Tuple

class PrimeCalculator(ABC):
    @abstractmethod
    def is_prime(self, n: int) -> bool:
        pass
    
    @abstractmethod
    def prime_factors(self, n: int) -> List[int]:
        pass
    
    @abstractmethod
    def gcd(self, a: int, b: int) -> int:
        pass
    
    @abstractmethod
    def lcm(self, a: int, b: int) -> int:
        pass
    
    @abstractmethod
    def sieve(self, limit: int) -> List[int]:
        pass
    
    @abstractmethod
    def goldbach(self, n: int) -> List[int]:
        pass
