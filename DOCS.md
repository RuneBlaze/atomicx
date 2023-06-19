# atomicx Documentation

atomicx is an easy-to-use atomics library for Python, providing atomic integer and boolean operations. This documentation provides an overview of the package and its usage.

## Installation

To install atomicx, use pip:

```bash
pip install atomicx
```

## Atomic Integer

The `AtomicInt` class provides atomic operations for 64-bit signed integers. Other integer types are not supported
for simplicity.

### Creation

To create an instance of `AtomicInt`, use the `AtomicInt()` constructor:

```python
from atomicx import AtomicInt

atom = AtomicInt() # Creates an atomic integer with an initial value of 0
```

You can also provide an initial value for the atomic integer:

```python
atom = AtomicInt(10)
```

### Atomic Operations

The `AtomicInt` class provides the following atomic operations:

- `load()`: Atomically loads the value of the atomic integer.
- `store(value)`: Atomically stores the given value into the atomic integer, returning the previous value.
- `add(value)`: Atomically adds the given value to the atomic integer, returning the previous value.
- `sub(value)`: Atomically subtracts the given value from the atomic integer, returning the previous value.
- `swap(value)`: Atomically swaps the value of the atomic integer with the given value.
- `compare_exchange(current, new)`: Atomically compares the value of the atomic integer with the given current value, and if they are equal, swaps it with the new value. Returns a boolean indicating whether the swap was successful and the previous value of the atomic integer.
- `mul(value)`: Atomically multiplies the atomic integer by the given value and returns the previous value.
- `div(value)`: Atomically divides the atomic integer by the given value and returns the previous value.

Here's an example of using some of these operations:

```python
atom = AtomicInt(5)
value = atom.load()
atom.add(10)
atom.swap(20)
```

### Increment and Decrement

The `AtomicInt` class provides convenience methods for incrementing and decrementing the atomic integer:

- `inc()`: Atomically increments the atomic integer by 1 and returns the previous value.
- `dec()`: Atomically decrements the atomic integer by 1 and returns the previous value.

Here's an example of using these methods:

```python
atom = AtomicInt(5)
previous_value = atom.inc()
```

### Compound Assignment Operations

The `AtomicInt` class supports compound assignment operations such as `+=`, `-=`, `*=`, and `/=`. These operations allow you to perform atomic modifications on the value of the `AtomicInt` instance.

```python
atom = AtomicInt(10)

atom += 5  # Atomic addition
atom -= 3  # Atomic subtraction
atom *= 2  # Atomic multiplication
atom /= 6  # Atomic division (raises divide by zero error if divisor is zero)
```

## Atomic Boolean

The `AtomicBool` class provides atomic operations for booleans.

### Creation

To create an instance of `AtomicBool`, use the `AtomicBool()` constructor:

```python
from atomicx import AtomicBool

atom = AtomicBool()
```

You can also provide an initial value for the atomic boolean:

```python
atom = AtomicBool(True)
```

### Atomic Operations

The `AtomicBool` class provides the following atomic operations:

- `load()`: Atomically loads the value of the atomic boolean.
- `store(value)`: Atomically stores the given value into the atomic boolean.
- `swap(value)`: Atomically swaps the value of the atomic boolean with the given value, returning the previous value.
- `compare_exchange(current, new)`: Atomically compares the value of the atomic boolean with the given current value, and if they are equal, swaps it with the new value. Returns a boolean indicating whether the swap was successful and the previous value of the atomic boolean.
- `flip()`: Atomically flips the value of the atomic boolean, returning the previous value.

Here's an example of using some of these operations:

```python
atom = AtomicBool(False)
value = atom.load()
atom.store(True)
atom.swap(False)
```