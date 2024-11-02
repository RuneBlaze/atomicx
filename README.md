# atomicx

[![PyPI version](https://badge.fury.io/py/atomicx.svg)](https://badge.fury.io/py/atomicx)

atomicx is an easy-to-use atomics library for Python, providing atomic integer, boolean, and floats. It allows you to perform atomic operations on shared variables, ensuring thread-safety and preventing race conditions in concurrent programming. Everything is entirely lock-free and is backed by Rust's atomic types.

## Features

- Atomic integer operations: load, store, add, subtract, swap, compare and exchange, multiply, divide, increment, decrement.
- Atomic boolean operations: load, store, swap, compare and exchange, flip.
- Atomic floats: load, store, swap, compare and exchange.
- Strong typing provided as stubs for static type checkers.

## Installation

Binary wheels are provided for Python 3.7 and above on Linux, macOS, and Windows:

```bash
pip install atomicx
```

## Usage

See the [documentation](DOCS.md) for more information. Here's a quick overview:

### Atomic Integer

```python
from atomicx import AtomicInt

# Create an atomic integer with an initial value of 0
atom = AtomicInt()

# Perform atomic operations
atom.store(10)
value = atom.load()
print(f"Value: {value}")

previous_value = atom.swap(20)
print(f"Previous Value: {previous_value}")

atom.add(5)
print(f"Result after addition: {atom}")

# Increment and decrement operations
atom.inc()
atom.dec()
```

### Atomic Boolean

```python
from atomicx import AtomicBool

# Create an atomic boolean with an initial value of False
atom = AtomicBool()

# Perform atomic operations
atom.store(True)
value = atom.load()
print(f"Value: {value}")

previous_value = atom.swap(False)
print(f"Previous Value: {previous_value}")

result = atom.compare_exchange(False, True)
print(f"Swap Result: {result}")

# Flip the value of the atomic boolean
atom.flip()
```

### Atomic Float

```python
from atomicx import AtomicFloat

# Create an atomic float with an initial value of 0.0
atom = AtomicFloat()
print(f"Initial Value: {atom.load()}")

# Perform atomic operations
atom.store(3.14)
value = atom.load()
print(f"Value: {value}")

# See docs for more operations
```

### Thread Safety

Atomic variables are thread-safe and can be shared between threads. Each predefined operation on them are executed per thread as an indivisible unit. Here's an example of using an atomic integer in a multithreaded environment:

```python
import threading
from atomicx import AtomicInt

x = AtomicInt(0)
def increment():
    for _ in range(1000):
        x.inc() # equivalent to x.add(1) or x += 1

threads = []
for _ in range(10):
    thread = threading.Thread(target=increment)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

assert x.load() == 1000 * 10
```

The equivalent in vanilla Python without locks is not thread-safe in general.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The `atomicx` library is heavily dependent on and inspired by the Rust `std::sync::atomic` module.
- The floating point atomic operations are delegated to the `portable-atomic` crate.