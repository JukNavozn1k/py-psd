from prime import (
    is_prime, prime_factors, gcd, lcm,
    sieve_of_eratosthenes, goldbach_conjecture
)

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(2) == True

def test_prime_factors():
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(28) == [2, 2, 7]
    assert prime_factors(1) == []

def test_gcd():
    assert gcd(18, 24) == 6
    assert gcd(54, 24) == 6
    assert gcd(7, 13) == 1

def test_lcm():
    assert lcm(6, 8) == 24
    assert lcm(3, 4) == 12
    assert lcm(2, 3) == 6

def test_sieve():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(1) == []
    
def test_goldbach():
    assert set(goldbach_conjecture(10)) == {3, 7}
    assert set(goldbach_conjecture(16)) == {5, 11}
    assert goldbach_conjecture(3) == []  # Not even number