from prime import (
    cpp_is_prime, cpp_prime_factors, cpp_gcd, cpp_lcm,
    cpp_sieve as sieve_of_eratosthenes, cpp_goldbach,
    CppPrimeError
)

class TestCppPrimeFunctions:
    def test_is_prime(self):
        assert cpp_is_prime(7) == True
        assert cpp_is_prime(10) == False
        assert cpp_is_prime(1) == False
        assert cpp_is_prime(2) == True

    def test_prime_factors(self):
        assert cpp_prime_factors(12) == [2, 2, 3]
        assert cpp_prime_factors(28) == [2, 2, 7]
        assert cpp_prime_factors(1) == []

    def test_gcd(self):
        assert cpp_gcd(18, 24) == 6
        assert cpp_gcd(54, 24) == 6
        assert cpp_gcd(7, 13) == 1

    def test_lcm(self):
        assert cpp_lcm(6, 8) == 24
        assert cpp_lcm(3, 4) == 12
        assert cpp_lcm(2, 3) == 6

    def test_sieve(self):
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
        assert sieve_of_eratosthenes(1) == []

    def test_goldbach(self):
        assert sorted(cpp_goldbach(28)) == [5, 23]
        assert sorted(cpp_goldbach(10)) == [3, 7]
