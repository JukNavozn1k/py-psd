# py-psd

Prime number calculations library with GUI and XML-RPC support.

## Installation

```bash
pip install poetry
poetry install
```

## Features

- Prime number checking
- Prime factorization
- GCD and LCM calculations
- Sieve of Eratosthenes
- Goldbach conjecture verification
- GUI interface
- XML-RPC server/client support

## XML-RPC Usage

1. Start the server:
```bash
python app/rpc_server.py
```

2. Use the client:
```python
from app.rpc_client import PrimeClient

client = PrimeClient()
is_prime = client.is_prime(17)
factors = client.prime_factors(28)
```

The server provides access to all prime number functions through RPC calls.