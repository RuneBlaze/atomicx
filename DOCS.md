# atomicx Documentation

atomicx is an easy-to-use atomics library for Python, providing atomic integer, boolean, and float operations. This documentation provides an overview of the package and its usage.

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

## Atomic Float

The `AtomicFloat` class provides atomic operations for 64-bit floating point numbers.

### Creation

To create an instance of `AtomicFloat`, use the `AtomicFloat()` constructor:

```python
from atomicx import AtomicFloat

atom = AtomicFloat()  # Creates with default value 0.0
```

You can also provide an initial value for the atomic float:

```python
atom = AtomicFloat(3.14)
```

### Atomic Operations

The `AtomicFloat` class provides the following atomic operations:

- `load()`: Atomically loads the value of the atomic float.
- `store(value)`: Atomically stores the given value into the atomic float.
- `add(value)`: Atomically adds the given value to the atomic float, returning the previous value.
- `sub(value)`: Atomically subtracts the given value from the atomic float, returning the previous value.
- `mul(value)`: Atomically multiplies the atomic float by the given value, returning the previous value.
- `div(value)`: Atomically divides the atomic float by the given value, returning the previous value. Raises `ZeroDivisionError` if the value is 0.
- `swap(value)`: Atomically swaps the value of the atomic float with the given value, returning the previous value.
- `compare_exchange(current, new)`: Atomically compares the value of the atomic float with the given current value, and if they are equal, swaps it with the new value. Returns a tuple of (success, previous_value) where success is a boolean indicating whether the swap was successful.

Here's an example of using some of these operations:

```python
atom = AtomicFloat(1.0)
value = atom.load()  # Gets current value
atom.store(2.5)     # Sets new value
prev = atom.add(1.5)  # Adds 1.5, returns previous value
prev = atom.mul(2.0)  # Multiplies by 2, returns previous value
```

### Arithmetic Operations

The `AtomicFloat` class supports in-place arithmetic operations:

```python
atom = AtomicFloat(1.0)
atom += 2.0  # Atomic addition
atom -= 1.0  # Atomic subtraction
```

### Thread Safety

All operations on `AtomicFloat` are atomic and thread-safe, making it suitable for use in concurrent applications:

```python
from threading import Thread

atom = AtomicFloat(0.0)

def worker():
    for _ in range(1000):
        atom.add(1.0)

threads = [Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(atom.load())  # Will reliably print 10000.0
```

### Special Methods

The class implements several special methods for convenience:

- `__repr__()`: Returns a string representation in the format `"AtomicFloat(value)"`
- `__str__()`: Returns the string representation of the current value
- `__float__()`: Allows conversion to a regular float value
- Support for pickling and unpickling