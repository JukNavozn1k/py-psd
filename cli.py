from prime import (
    py_is_prime, py_prime_factors, py_gcd, py_lcm, 
    py_sieve, py_goldbach,
    cpp_is_prime, cpp_prime_factors, cpp_gcd, cpp_lcm,
    cpp_sieve, cpp_goldbach,
    PrimeError, NegativeNumberError, InvalidInputError, NumberTooLargeError,
    CppPrimeError
)
from rpc import PrimeClient

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
        # C++ implementation
        "cpp_is_prime": cpp_is_prime,
        "cpp_prime_factors": cpp_prime_factors,
        "cpp_gcd": cpp_gcd,
        "cpp_lcm": cpp_lcm,
        "cpp_sieve": cpp_sieve,
        "cpp_goldbach": cpp_goldbach,
        # RPC functions
        "rpc_is_prime": create_rpc_wrapper("is_prime"),
        "rpc_prime_factors": create_rpc_wrapper("prime_factors"),
        "rpc_gcd": create_rpc_wrapper("gcd"),
        "rpc_lcm": create_rpc_wrapper("lcm"),
        "rpc_sieve": create_rpc_wrapper("sieve"),
        "rpc_goldbach": create_rpc_wrapper("goldbach"),
        # Exceptions
        "PrimeError": PrimeError,
        "NegativeNumberError": NegativeNumberError,
        "InvalidInputError": InvalidInputError,
        "CppPrimeError": CppPrimeError,
    }
    try:
        return eval(expr, allowed_globals, allowed_locals)
    except (PrimeError, CppPrimeError) as e:
        raise InvalidInputError(str(e))
    except Exception as e:
        raise InvalidInputError(f"Invalid expression: {e}")

def cli():
    print("=== Prime CLI ===")
    print("Available functions:")
    print("Python implementation:")
    print("  py_is_prime(n), py_prime_factors(n), py_gcd(a,b),")
    print("  py_lcm(a,b), py_sieve(limit), py_goldbach(n)")
    print("C++ implementation:")
    print("  cpp_is_prime(n), cpp_prime_factors(n), cpp_gcd(a,b),")
    print("  cpp_lcm(a,b), cpp_sieve(limit), cpp_goldbach(n)")
    print("RPC functions:")
    print("  rpc_is_prime(n), rpc_prime_factors(n), rpc_gcd(a,b),")
    print("  rpc_lcm(a,b), rpc_sieve(limit), rpc_goldbach(n)")
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
            result = safe_eval(expr)
            print(f"Result: {result}")
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
