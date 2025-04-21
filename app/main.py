import tkinter as tk
from tkinter import ttk, messagebox
from prime import is_prime, prime_factors, gcd, lcm, sieve_of_eratosthenes, goldbach_conjecture

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

        # Rest of the GUI code remains the same, just change parent from root to main_container
        input_frame = ttk.LabelFrame(main_container, text="Input", padding="10")
        # Additional GUI elements can be added here

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimeCalculator(root)
    root.mainloop()