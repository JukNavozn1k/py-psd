from xmlrpc.server import SimpleXMLRPCServer
from prime.prime import (
    is_prime, prime_factors, gcd, lcm,
    sieve_of_eratosthenes, goldbach_conjecture
)

def start_server(host="localhost", port=8000):
    server = SimpleXMLRPCServer((host, port))
    print(f"Listening on {host}:{port}...")

    # Register all prime functions
    server.register_function(is_prime, "is_prime")
    server.register_function(prime_factors, "prime_factors")
    server.register_function(gcd, "gcd")
    server.register_function(lcm, "lcm")
    server.register_function(sieve_of_eratosthenes, "sieve")
    server.register_function(goldbach_conjecture, "goldbach")

    # Start the server
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == "__main__":
    start_server()
