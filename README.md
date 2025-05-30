# Библиотека для работы с простыми числами

Набор инструментов для различных вычислений, связанных с простыми числами.

## Установка

```bash
pip install poetry
poetry install
```

## Возможности

- Проверка числа на простоту
- Разложение числа на простые множители
- Вычисление НОД (наибольший общий делитель)
- Вычисление НОК (наименьшее общее кратное)
- Поиск простых чисел в диапазоне (решето Эратосфена)
- Проверка гипотезы Гольдбаха

## Как использовать

### Через графический интерфейс
```bash
python main.py
```

### Через командную строку
```bash
python cli.py
```

### Через сетевой доступ (XML-RPC)

1. Запустите сервер:
```bash
python -m rpc.rpc_server
```

2. Используйте клиент в своём коде:
```python
from rpc import PrimeClient

client = PrimeClient()
# Проверить, простое ли число
result = client.is_prime(17)
# Получить множители числа
factors = client.prime_factors(28)
```

## Лицензия

MIT License - можно свободно использовать код в любых целях с указанием авторства.