from prime import (
    py_is_prime, py_prime_factors, py_gcd, py_lcm, 
    py_sieve, py_goldbach, py_ferma_test,
    c_is_prime, c_prime_factors, c_gcd, c_lcm,
    c_sieve, c_goldbach, c_ferma_test,
    PrimeError, NegativeNumberError, InvalidInputError, NumberTooLargeError,
    CPrimeError
)
from rpc import PrimeClient
import time

def create_rpc_wrapper(func_name):
    def wrapper(*args):
        try:
            client = PrimeClient()
            return getattr(client, func_name)(*args)
        except ConnectionError:
            raise InvalidInputError("RPC server is not available")
    return wrapper

def safe_eval(expr: str) -> any:
    allowed_globals = {
        "__builtins__": None,
    }
    allowed_locals = {
        # Python implementation
        "py_is_prime": py_is_prime,
        "py_prime_factors": py_prime_factors,
        "py_gcd": py_gcd,
        "py_lcm": py_lcm,
        "py_sieve": py_sieve,
        "py_goldbach": py_goldbach,
        "py_ferma_test": py_ferma_test,
        # C implementation
        "c_is_prime": c_is_prime,
        "c_prime_factors": c_prime_factors,
        "c_gcd": c_gcd,
        "c_lcm": c_lcm,
        "c_sieve": c_sieve,
        "c_goldbach": c_goldbach,
        "c_ferma_test": c_ferma_test,
        # RPC functions
        "rpc_is_prime": create_rpc_wrapper("is_prime"),
        "rpc_prime_factors": create_rpc_wrapper("prime_factors"),
        "rpc_gcd": create_rpc_wrapper("gcd"),
        "rpc_lcm": create_rpc_wrapper("lcm"),
        "rpc_sieve": create_rpc_wrapper("sieve"),
        "rpc_goldbach": create_rpc_wrapper("goldbach"),
        "rpc_ferma_test": create_rpc_wrapper("ferma_test"),
        # Exceptions
        "PrimeError": PrimeError,
        "NegativeNumberError": NegativeNumberError,
        "InvalidInputError": InvalidInputError,
        "CPrimeError": CPrimeError,
    }
    try:
        return eval(expr, allowed_globals, allowed_locals)
    except (PrimeError, CPrimeError) as e:
        raise InvalidInputError(str(e))
    except Exception as e:
        raise InvalidInputError(f"Invalid expression: {e}")

def cli():
    print("=== Prime CLI ===")
    print("Available functions:")
    print("Python implementation:")
    print("  py_is_prime(n), py_prime_factors(n), py_gcd(a,b),")
    print("  py_lcm(a,b), py_sieve(limit), py_goldbach(n), py_ferma_test(n)")
    print("C implementation:")
    print("  c_is_prime(n), c_prime_factors(n), c_gcd(a,b),")
    print("  c_lcm(a,b), c_sieve(limit), c_goldbach(n), c_ferma_test(n)")
    print("RPC functions:")
    print("  rpc_is_prime(n), rpc_prime_factors(n), rpc_gcd(a,b),")
    print("  rpc_lcm(a,b), rpc_sieve(limit), rpc_goldbach(n), rpc_ferma_test(n)")
    print("Type 'exit' or 'quit' to exit.")
    print("=================")

    while True:
        expr = input(">>> ").strip()
        if expr.lower() in {"exit", "quit"}:
            print("Exiting Prime CLI. Goodbye!")
            break
        if not expr:
            continue
        try:
            start_time = time.perf_counter()
            result = safe_eval(expr)
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Result: {result}")
            print(f"Execution time: {execution_time:.2f} ms")
        except NegativeNumberError as e:
            print(f"[NegativeNumberError] {e}")
        except InvalidInputError as e:
            print(f"[InvalidInputError] {e}")
        except NumberTooLargeError as e:
            print(f"[NumberTooLargeError] {e}")
        except PrimeError as e:
            print(f"[PrimeError] {e}")
        except Exception as e:
            print(f"[UnknownError] {e}")

if __name__ == "__main__":
    cli()
