#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <cstdint>

namespace py = pybind11;

using BigInt = __int128;  // Для очень больших чисел

std::string to_string(BigInt n) {
    if (n == 0) return "0";
    bool neg = n < 0;
    if (neg) n = -n;
    std::string res;
    while (n > 0) {
        res += '0' + (n % 10);
        n /= 10;
    }
    if (neg) res += '-';
    std::reverse(res.begin(), res.end());
    return res;
}

void validate_positive(BigInt n, const std::string& operation) {
    if (n < 0) {
        throw std::invalid_argument("Number cannot be negative for " + operation);
    }
}

bool is_prime(BigInt n) {
    validate_positive(n, "primality test");
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    BigInt i = 5;
    BigInt w = 2;
    while (i * i <= n) {
        if (n % i == 0) return false;
        i += w;
        w = 6 - w;
    }
    return true;
}

std::vector<BigInt> prime_factors(BigInt n) {
    validate_positive(n, "prime factorization");
    if (n == 0) {
        throw std::invalid_argument("Cannot factorize zero");
    }
    std::vector<BigInt> factors;
    for (BigInt divisor : {2, 3}) {
        while (n % divisor == 0) {
            factors.push_back(divisor);
            n /= divisor;
        }
    }
    BigInt i = 5;
    BigInt w = 2;
    while (i * i <= n) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
        i += w;
        w = 6 - w;
    }
    if (n > 1) {
        factors.push_back(n);
    }
    return factors;
}

BigInt gcd(BigInt a, BigInt b) {
    validate_positive(a, "GCD");
    validate_positive(b, "GCD");
    if (a == 0 && b == 0) {
        throw std::invalid_argument("GCD is undefined for (0,0)");
    }
    while (b != 0) {
        BigInt temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

BigInt lcm(BigInt a, BigInt b) {
    validate_positive(a, "LCM");
    validate_positive(b, "LCM");
    if (a == 0 || b == 0) {
        throw std::invalid_argument("LCM is undefined for zero");
    }
    return a / gcd(a, b) * b;
}

std::vector<BigInt> sieve_of_eratosthenes(BigInt limit) {
    validate_positive(limit, "sieve of Eratosthenes");
    if (limit > (1 << 20)) {
        throw std::invalid_argument("Limit too large for sieve");
    }
    if (limit < 2) return {};
    std::vector<bool> sieve(limit + 1, true);
    sieve[0] = sieve[1] = false;
    for (BigInt num = 2; num * num <= limit; ++num) {
        if (sieve[num]) {
            for (BigInt j = num * num; j <= limit; j += num) {
                sieve[j] = false;
            }
        }
    }
    std::vector<BigInt> primes;
    for (BigInt i = 2; i <= limit; ++i) {
        if (sieve[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

std::pair<BigInt, BigInt> goldbach_conjecture(BigInt n) {
    validate_positive(n, "Goldbach conjecture");
    if (n <= 2 || n % 2 != 0) {
        throw std::invalid_argument("Number must be even and > 2 for Goldbach conjecture");
    }
    auto primes = sieve_of_eratosthenes(n);
    std::unordered_set<BigInt> prime_set(primes.begin(), primes.end());
    for (BigInt p : primes) {
        if (prime_set.count(n - p)) {
            return {p, n - p};
        }
    }
    return {0, 0};  // Не найдено
}

PYBIND11_MODULE(prime_module, m) {
    m.doc() = "Prime number operations with big integer support";

    m.def("is_prime", &is_prime);
    m.def("prime_factors", &prime_factors);
    m.def("gcd", &gcd);
    m.def("lcm", &lcm);
    m.def("sieve_of_eratosthenes", &sieve_of_eratosthenes);
    m.def("goldbach_conjecture", &goldbach_conjecture);

    m.def("to_string", &to_string, "Convert BigInt to string");
}
