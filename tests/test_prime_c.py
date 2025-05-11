from prime import (
    c_is_prime,
    c_prime_factors,
    c_gcd,
    c_lcm,
    c_sieve,
    c_goldbach,
    CPrimeError,
    c_ferma_test
)

class TestcPrimeFunctions:
    def test_is_prime(self):
        assert c_is_prime(7) == True
        assert c_is_prime(10) == False
        assert c_is_prime(1) == False
        assert c_is_prime(2) == True

    def test_prime_factors(self):
        assert c_prime_factors(12) == [2, 2, 3]
        assert c_prime_factors(28) == [2, 2, 7]
        assert c_prime_factors(1) == []

    def test_gcd(self):
        assert c_gcd(18, 24) == 6
        assert c_gcd(54, 24) == 6
        assert c_gcd(7, 13) == 1

    def test_lcm(self):
        assert c_lcm(6, 8) == 24
        assert c_lcm(3, 4) == 12
        assert c_lcm(2, 3) == 6

    def test_sieve(self):
        assert c_sieve(10) == [2, 3, 5, 7]
        assert c_sieve(1) == []

    def test_goldbach(self):
        assert sorted(c_goldbach(28)) == [5, 23]
        assert sorted(c_goldbach(10)) == [3, 7]
