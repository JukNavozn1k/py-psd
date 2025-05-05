from prime import (
    py_is_prime, py_prime_factors, py_gcd, py_lcm, 
    py_sieve, py_goldbach, py_ferma_test,
    cpp_is_prime, cpp_prime_factors, cpp_gcd, cpp_lcm,
    cpp_sieve, cpp_goldbach, cpp_ferma_test,
    PrimeError, NegativeNumberError, InvalidInputError, NumberTooLargeError,
    CppPrimeError
)
import time

start_num = 1024
py_times = []
cpp_times = []

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
py_times = run_prime_benchmark(py_sieve,1000)
cpp_times = run_prime_benchmark(cpp_sieve,1000)
print(f'Python exec times: {py_times[-10:]}')
print(f'Cpp exec times {cpp_times[-10:]}')


