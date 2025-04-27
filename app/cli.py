from prime.prime import (
    is_prime, prime_factors, gcd, lcm, 
    sieve_of_eratosthenes, goldbach_conjecture,
    PrimeError, NegativeNumberError, InvalidInputError
)

def safe_eval(expr: str) -> any:
    allowed_globals = {
        "__builtins__": None,
    }
    allowed_locals = {
        "is_prime": is_prime,
        "prime_factors": prime_factors,
        "gcd": gcd,
        "lcm": lcm,
        "sieve_of_eratosthenes": sieve_of_eratosthenes,
        "goldbach_conjecture": goldbach_conjecture,
        "PrimeError": PrimeError,
        "NegativeNumberError": NegativeNumberError,
        "InvalidInputError": InvalidInputError,
    }
    try:
        return eval(expr, allowed_globals, allowed_locals)
    except PrimeError as e:
        raise e  # Наши кастомные ошибки
    except Exception as e:
        raise InvalidInputError(f"Invalid expression: {e}")

def cli():
    print("=== Prime CLI ===")
    print("Available functions: is_prime(n), prime_factors(n), gcd(a, b), lcm(a, b),")
    print("sieve_of_eratosthenes(limit), goldbach_conjecture(n)")
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
