import tkinter as tk
from tkinter import ttk, messagebox
from prime import is_prime, prime_factors, gcd, lcm, sieve_of_eratosthenes

class PrimeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Prime Number Calculator")
        self.root.geometry("600x400")
        
        # Configure window scaling
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Main container
        main_container = ttk.Frame(root)
        main_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        main_container.grid_columnconfigure(0, weight=1)
        for i in range(4):
            main_container.grid_rowconfigure(i, weight=1)

        # Input frame
        input_frame = ttk.LabelFrame(main_container, text="Input", padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        ttk.Label(input_frame, text="Enter number:").grid(row=0, column=0, padx=5)
        self.number_entry = ttk.Entry(input_frame)
        self.number_entry.grid(row=0, column=1, padx=5)

        # Buttons frame
        buttons_frame = ttk.LabelFrame(main_container, text="Operations", padding="10")
        buttons_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        ttk.Button(buttons_frame, text="Check Prime", command=self.check_prime).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(buttons_frame, text="Prime Factors", command=self.get_factors).grid(row=0, column=1, padx=5, pady=5)

        # Two number operations frame
        two_num_frame = ttk.LabelFrame(main_container, text="Two Number Operations", padding="10")
        two_num_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        ttk.Label(two_num_frame, text="First number:").grid(row=0, column=0, padx=5)
        self.num1_entry = ttk.Entry(two_num_frame)
        self.num1_entry.grid(row=0, column=1, padx=5)

        ttk.Label(two_num_frame, text="Second number:").grid(row=1, column=0, padx=5)
        self.num2_entry = ttk.Entry(two_num_frame)
        self.num2_entry.grid(row=1, column=1, padx=5)

        ttk.Button(two_num_frame, text="Calculate GCD", command=self.calculate_gcd).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(two_num_frame, text="Calculate LCM", command=self.calculate_lcm).grid(row=2, column=1, padx=5, pady=5)

        # Result frame
        result_frame = ttk.LabelFrame(main_container, text="Result", padding="10")
        result_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

        self.result_text = tk.Text(result_frame, height=5, width=50)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)

    def get_number(self):
        try:
            return int(self.number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            return None

    def get_two_numbers(self):
        try:
            n1 = int(self.num1_entry.get())
            n2 = int(self.num2_entry.get())
            return n1, n2
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers")
            return None, None

    def check_prime(self):
        n = self.get_number()
        if n is not None:
            result = "Prime" if is_prime(n) else "Not Prime"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

    def get_factors(self):
        n = self.get_number()
        if n is not None:
            factors = prime_factors(n)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(factors))


    def calculate_gcd(self):
        n1, n2 = self.get_two_numbers()
        if n1 is not None and n2 is not None:
            result = gcd(n1, n2)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(result))

    def calculate_lcm(self):
        n1, n2 = self.get_two_numbers()
        if n1 is not None and n2 is not None:
            result = lcm(n1, n2)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimeCalculator(root)
    root.mainloop()