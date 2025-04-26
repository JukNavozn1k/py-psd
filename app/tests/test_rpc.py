import threading
import time
from app.rpc_client import PrimeClient  
from app.rpc_server import start_server 

class TestPrimeRPC:
    @classmethod
    def setup_class(cls):
        cls.server_thread = threading.Thread(target=start_server, daemon=True)
        cls.server_thread.start()

        time.sleep(1) 
        cls.client = PrimeClient()

    @classmethod
    def teardown_class(cls):
        pass  

    def test_is_prime(self):
        assert self.client.is_prime(7) is True
        assert self.client.is_prime(10) is False
        assert self.client.is_prime(1) is False
        assert self.client.is_prime(2) is True

    def test_prime_factors(self):
        assert self.client.prime_factors(12) == [2, 2, 3]
        assert self.client.prime_factors(28) == [2, 2, 7]
        assert self.client.prime_factors(1) == []

    def test_gcd(self):
        assert self.client.gcd(18, 24) == 6
        assert self.client.gcd(54, 24) == 6
        assert self.client.gcd(7, 13) == 1

    def test_lcm(self):
        assert self.client.lcm(6, 8) == 24
        assert self.client.lcm(3, 4) == 12
        assert self.client.lcm(2, 3) == 6

    def test_sieve(self):
        assert self.client.sieve(10) == [2, 3, 5, 7]
        assert self.client.sieve(1) == []

    def test_goldbach(self):
        assert sorted(self.client.goldbach(28)) == [5, 23]
        assert sorted(self.client.goldbach(10)) == [3, 7]
