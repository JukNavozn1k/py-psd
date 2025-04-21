from .prime import *
# Примеры использования
if __name__ == "__main__":
    print("Проверка на простоту:")
    print(f"7 → {is_prime(7)}")       # True
    print(f"10 → {is_prime(10)}")     # False

    print("\nРазложение на множители:")
    print(f"12 → {prime_factors(12)}")  # [2, 2, 3]
    print(f"28 → {prime_factors(28)}")  # [2, 2, 7]

    print("\nНОД и НОК:")
    print(f"НОД(18, 24) → {gcd(18, 24)}")  # 6
    print(f"НОК(6, 8) → {lcm(6, 8)}")      # 24

    print("\nРешето Эратосфена до 30:")
    print(sieve_of_eratosthenes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    print("\nГипотеза Гольдбаха:")
    print(f"10 → {goldbach_conjecture(10)}")  # [3, 7]
    print(f"16 → {goldbach_conjecture(16)}")  # [5, 11]