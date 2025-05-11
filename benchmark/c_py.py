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
py_times = run_prime_benchmark(py_sieve,191919)
c_times = run_prime_benchmark(c_sieve,191919)
print(f'C times: {c_times[-1]}')
print(f'Py times {py_times[-1]}')



# # 1024-битное простое число (309 цифр)
# large_prime_1 = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137859

# # 512-битное простое число (155 цифр)
# large_prime_2 = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

# # 256-битное простое число (78 цифр)
# large_prime_3 = 115792089237316195423570985008687907853269984665640564039457584007913129640233

