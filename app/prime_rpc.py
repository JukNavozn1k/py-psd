from xmlrpc.client import ServerProxy
from .prime_interface import PrimeCalculator

class RPCPrimeCalculator(PrimeCalculator):
    def __init__(self, host: str = "localhost", port: int = 8000):
        self.server = ServerProxy(f"http://{host}:{port}/")
    
    def is_prime(self, n: int) -> bool:
        return self.server.is_prime(n)
    
    def prime_factors(self, n: int) -> list[int]:
        return self.server.prime_factors(n)
    
    def gcd(self, a: int, b: int) -> int:
        return self.server.gcd(a, b)
    
    def lcm(self, a: int, b: int) -> int:
        return self.server.lcm(a, b)
    
    def sieve(self, limit: int) -> list[int]:
        return self.server.sieve(limit)
    
    def goldbach(self, n: int) -> list[int]:
        return self.server.goldbach(n)
