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

from prime import (
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


import time

start_num = 1024
py_times = []
c_times = []

def run_prime_benchmark(method,iterations=10):
    times = []
    for i in range(10):
        start_time = time.perf_counter()
        method(start_num * (2**i))
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        times.append(execution_time)
    return times
print('Time in ms')
py_times = run_prime_benchmark(py_prime_factors,1500)
c_times = run_prime_benchmark(c_prime_factors,1500)
print(f'C times: {c_times[-10:]}')
print(f'Py times {py_times[-10:]}')

