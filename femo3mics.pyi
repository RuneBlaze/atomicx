from typing import Any, Callable, Generic, Optional, Tuple, TypeVar
class AtomicInt:
    """
    Represents an atomic signed integer of 64 bits. Unsigned or other widths are not supported for simplicity.
    """

    def __init__(self, value: int = 0) -> 'AtomicInt':
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

    def fetch_mul(self, value: int) -> int:
        """
        Atomically multiplies the atomic integer by the given value and returns the previous value.

        Args:
            value: The value to multiply with the atomic integer.

        Returns:
            The previous value of the atomic integer.
        """
        ...

    def fetch_div(self, value: int) -> int:
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

class AtomicBool:
    """
    Represents an atomic boolean.
    """

    def __init__(self, value: bool = False) -> 'AtomicBool':
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