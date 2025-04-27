from prime import (
    is_prime, prime_factors, gcd, lcm, 
    sieve_of_eratosthenes, goldbach_conjecture,
    PrimeError, NegativeNumberError, InvalidInputError
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
        # Local functions
        "local_is_prime": is_prime,
        "local_prime_factors": prime_factors,
        "local_gcd": gcd,
        "local_lcm": lcm,
        "local_sieve": sieve_of_eratosthenes,
        "local_goldbach": goldbach_conjecture,
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
    }
    try:
        return eval(expr, allowed_globals, allowed_locals)
    except PrimeError as e:
        raise e
    except Exception as e:
        raise InvalidInputError(f"Invalid expression: {e}")

def cli():
    print("=== Prime CLI ===")
    print("Available functions:")
    print("Local functions: local_is_prime(n), local_prime_factors(n),")
    print("  local_gcd(a,b), local_lcm(a,b), local_sieve(limit), local_goldbach(n)")
    print("RPC functions: rpc_is_prime(n), rpc_prime_factors(n),")
    print("  rpc_gcd(a,b), rpc_lcm(a,b), rpc_sieve(limit), rpc_goldbach(n)")
    print("Type 'exit' or 'quit' to exit.")
    print("=================")

    while True:
        expr = input(">>> ").strip()
        if expr.lower() in {"exit", "quit"}:
            print("Exiting Prime CLI. Goodbye!")
            break
        if not expr:
            continue  # Пустой ввод пропускаем
        try:
            result = safe_eval(expr)
            print(f"Result: {result}")
        except NegativeNumberError as e:
            print(f"[NegativeNumberError] {e}")
        except InvalidInputError as e:
            print(f"[InvalidInputError] {e}")
        except PrimeError as e:
            print(f"[PrimeError] {e}")
        except Exception as e:
            print(f"[UnknownError] {e}")

if __name__ == "__main__":
    cli()
