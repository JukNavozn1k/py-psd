from xmlrpc.client import ServerProxy

class PrimeClient:
    def __init__(self, host="localhost", port=8000):
        self.server = ServerProxy(f"http://{host}:{port}/")

    def is_prime(self, n):
        return self.server.is_prime(n)

    def prime_factors(self, n):
        return self.server.prime_factors(n)

    def gcd(self, a, b):
        return self.server.gcd(a, b)

    def lcm(self, a, b):
        return self.server.lcm(a, b)

    def sieve(self, limit):
        return self.server.sieve(limit)

    def goldbach(self, n):
        return self.server.goldbach(n)

if __name__ == "__main__":
    # Example usage
    client = PrimeClient()
    
    # Test some functions
    print(f"Is 17 prime? {client.is_prime(17)}")
    print(f"Prime factors of 28: {client.prime_factors(28)}")
    print(f"GCD of 48 and 18: {client.gcd(48, 18)}")
    print(f"LCM of 15 and 20: {client.lcm(15, 20)}")
    print(f"Primes up to 20: {client.sieve(20)}")
    print(f"Goldbach pair for 28: {client.goldbach(28)}")
