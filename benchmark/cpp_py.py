from prime import (
    cpp_is_prime,
    cpp_prime_factors,
    cpp_gcd,
    cpp_lcm,
    cpp_sieve,
    cpp_goldbach,
    CppPrimeError,
    cpp_ferma_test,
    py_sieve
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
py_times = run_prime_benchmark(cpp_sieve,1500)
cpp_times = run_prime_benchmark(py_sieve,1500)
print(f'Cpp exec times: {py_times[-10:]}')
print(f'Py exec times {cpp_times[-10:]}')


