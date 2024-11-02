"""
atomicx is an easy-to-use atomics library for Python, providing atomic integer and boolean operations for thread-safe programming.

The package includes two main classes: `AtomicInt` and `AtomicBool`, which allow you to perform atomic operations on shared variables, ensuring thread-safety and preventing race conditions in concurrent programming.

- `AtomicInt` provides atomic operations such as load, store, add, subtract, swap, compare and exchange, multiply, divide, increment, and decrement for integer variables.
- `AtomicBool` provides atomic operations such as load, store, swap, compare and exchange, and flip for boolean variables.
- `AtomicFloat` provides atomic operations for floating-point numbers.

Integer and boolean atomics are backed by `std::sync::atomic`, while floating-point atomics are delegated to the `portable-atomic` crate.
Note that many operations for floating point atomics are underlyingly implemented
using CAS (compare-and-swap) loops.
"""

from typing import Any, Callable, Generic, Optional, Tuple, TypeVar

class AtomicInt:
    """
    Represents an atomic signed integer of 64 bits. Unsigned or other widths are not supported for simplicity.
    """

    def __init__(self, value: int = 0) -> "AtomicInt":
        """
        Creates a new instance of AtomicInt.

        Args:
            value: The initial value of the atomic integer. Defaults to 0.

        Returns:
            An instance of AtomicInt.
        """
        ...

    def load(self) -> int:
        """
        Atomically loads the value of the atomic integer.

        Returns:
            The current value of the atomic integer.
        """
        ...

    def store(self, value: int) -> None:
        """
        Atomically stores the given value into the atomic integer.

        Args:
            value: The value to store.
        """
        ...

    def add(self, value: int) -> int:
        """
        Atomically adds the given value to the atomic integer.

        Args:
            value: The value to add.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def sub(self, value: int) -> int:
        """
        Atomically subtracts the given value from the atomic integer.

        Args:
            value: The value to subtract.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def swap(self, value: int) -> int:
        """
        Atomically swaps the value of the atomic integer with the given value.

        Args:
            value: The value to swap.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def compare_exchange(self, current: int, new: int) -> Tuple[bool, int]:
        """
        Atomically compares the value of the atomic integer with the given current value,
        and if they are equal, swaps it with the new value.

        Args:
            current: The expected current value of the atomic integer.
            new: The value to swap if the current value matches.

        Returns:
            A tuple containing a boolean indicating if the swap was successful,
            and the previous value of the atomic integer.
        """
        ...

    def mul(self, value: int) -> int:
        """
        Atomically multiplies the atomic integer by the given value and returns the previous value.

        Args:
            value: The value to multiply with the atomic integer.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def div(self, value: int) -> int:
        """
        Atomically divides the atomic integer by the given value and returns the result.

        Args:
            value: The value to divide the atomic integer by.

        Returns:
            The result of the division.

        Raises:
            ZeroDivisionError: If the given value is zero.
        """
        ...

    def inc(self) -> int:
        """
        Atomically increments the atomic integer by 1.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def dec(self) -> int:
        """
        Atomically decrements the atomic integer by 1.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def __getstate__(self) -> float: ...
    def __setstate__(self, value: float) -> None: ...

class AtomicBool:
    """
    Represents an atomic boolean.
    """

    def __init__(self, value: bool = False) -> "AtomicBool":
        """
        Creates a new instance of AtomicBool.

        Args:
            value: The initial value of the atomic boolean. Defaults to False.

        Returns:
            An instance of AtomicBool.
        """
        ...

    def load(self) -> bool:
        """
        Atomically loads the value of the atomic boolean.

        Returns:
            The current value of the atomic boolean.
        """
        ...

    def store(self, value: bool) -> None:
        """
        Atomically stores the given value into the atomic boolean.

        Args:
            value: The value to store.
        """
        ...

    def swap(self, value: bool) -> bool:
        """
        Atomically swaps the value of the atomic boolean with the given value.

        Args:
            value: The value to swap.

        Returns:
            The previous value of the atomic boolean.
        """
        ...

    def compare_exchange(self, current: bool, new: bool) -> Tuple[bool, bool]:
        """
        Atomically compares the value of the atomic boolean with the given current value,
        and if they are equal, swaps it with the new value.

        Args:
            current: The expected current value of the atomic boolean.
            new: The value to swap if the current value matches.

        Returns:
            A tuple containing a boolean indicating if the swap was successful,
            and the previous value of the atomic boolean.
        """
        ...

    def flip(self) -> bool:
        """
        Atomically flips the value of the atomic boolean.

        Returns:
            The previous value of the atomic boolean.
        """
        ...

    def __getstate__(self) -> float: ...
    def __setstate__(self, value: float) -> None: ...

class AtomicFloat:
    """An atomic floating-point number that can be safely shared between threads.

    Note: This class is implemented using the `portable-atomic` crate, and under the hood, many operations are implemented using CAS (compare-and-swap) loops.

    Args:
        value: Initial floating-point value. Defaults to 0.0.
    """

    def __init__(self, value: float = 0.0) -> None: ...
    def load(self) -> float:
        """Atomically loads the current value.

        Returns:
            float: The current value.
        """
        ...

    def store(self, value: float) -> None:
        """Atomically stores a new value.

        Args:
            value: The value to store.
        """
        ...

    def add(self, value: float) -> float:
        """Atomically adds a value and returns the previous value.

        Args:
            value: The value to add.

        Returns:
            float: The value before the addition.
        """
        ...

    def sub(self, value: float) -> float:
        """Atomically subtracts a value and returns the previous value.

        Args:
            value: The value to subtract.

        Returns:
            float: The value before the subtraction.
        """
        ...

    def swap(self, value: float) -> float:
        """Atomically replaces the current value and returns the previous value.

        Args:
            value: The new value to store.

        Returns:
            float: The previous value.
        """
        ...

    def compare_exchange(self, current: float, new: float) -> Tuple[bool, float]:
        """Atomically compares and exchanges values.

        Compares the current value with the expected value and, if equal,
        replaces it with the new value.

        Args:
            current: The expected current value.
            new: The new value to store if current matches.

        Returns:
            Tuple[bool, float]: A tuple containing:
                - bool: True if the exchange was successful
                - float: The actual current value (either before or after exchange)
        """
        ...

    def mul(self, value: float) -> float:
        """Atomically multiplies by a value and returns the previous value.

        Args:
            value: The value to multiply by.

        Returns:
            float: The value before multiplication.
        """
        ...

    def div(self, value: float) -> float:
        """Atomically divides by a value and returns the previous value.

        Args:
            value: The value to divide by.

        Raises:
            ZeroDivisionError: If value is 0.

        Returns:
            float: The value before division.
        """
        ...

    def __iadd__(self, value: float) -> None: ...
    def __isub__(self, value: float) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __float__(self) -> float: ...
    def __getstate__(self) -> float: ...
    def __setstate__(self, value: float) -> None: ...
