# feo3mics

[![PyPI version](https://badge.fury.io/py/feo3mics.svg)](https://badge.fury.io/py/feo3mics)

feo3mics is an easy-to-use atomics library for Python, providing atomic integer and boolean operations. It allows you to perform atomic operations on shared variables, ensuring thread-safety and preventing race conditions in concurrent programming. Everything is entirely lock-free and is backed by Rust's atomic types.

## Features

- Atomic integer operations: load, store, add, subtract, swap, compare and exchange, multiply, divide, increment, decrement.
- Atomic boolean operations: load, store, swap, compare and exchange, flip.

## Installation

```bash
pip install feo3mics
```

## Usage

See the [documentation](DOCS.md) for more information. Here's a quick overview:

### Atomic Integer

```python
from feo3mics import AtomicInt

# Create an atomic integer with an initial value of 0
atom = AtomicInt()

# Perform atomic operations
atom.store(10)
value = atom.load()
print(f"Value: {value}")

previous_value = atom.swap(20)
print(f"Previous Value: {previous_value}")

result = atom.add(5)
print(f"Result: {result}")

# Increment and decrement operations
atom.inc()
atom.dec()
```

### Atomic Boolean

```python
from feo3mics import AtomicBool

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The `feo3mics` library is heavily dependent on and inspired by the Rust `std::sync::atomic` module.