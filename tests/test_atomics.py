import threading
from atomicx import AtomicInt, AtomicBool, AtomicFloat
import pytest

import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def test_atomic_int_increment():
    atom = AtomicInt()

    def increment_atomic():
        for _ in range(1000):
            atom.inc()

    # Create multiple threads to increment the atomic integer concurrently
    threads = []
    for _ in range(10):
        t = threading.Thread(target=increment_atomic)
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # The expected value should be the number of threads multiplied by the number of increments per thread
    expected_value = 10 * 1000
    assert atom.load() == expected_value


def test_atomic_int_add_race_condition():
    atom = AtomicInt()

    def add_to_atomic(value):
        for _ in range(1000):
            atom.add(value)

    # Create multiple threads to concurrently add to the atomic integer
    threads = []
    for i in range(10):
        t = threading.Thread(target=add_to_atomic, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # The expected value should be the sum of 0 + 1 + 2 + ... + 9 multiplied by the number of increments per thread
    expected_value = sum(range(10)) * 1000
    assert atom.load() == expected_value


def test_atomic_int_race_condition_with_non_atomic_operations():
    atom = AtomicInt()

    def non_atomic_operation():
        for _ in range(1000):
            current_value = atom.load()
            # Simulate a non-atomic operation (e.g., time-consuming calculation)
            # before updating the atomic integer
            result = current_value * 2
            atom.store(result)

    # Create multiple threads to perform non-atomic operations and update the atomic integer concurrently
    threads = []
    for _ in range(10):
        t = threading.Thread(target=non_atomic_operation)
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # The expected value should be the result of the non-atomic operation applied multiple times
    expected_value = 0
    for _ in range(1000):
        expected_value = expected_value * 2
    assert atom.load() == expected_value


def test_atomic_bool_compare_exchange_successful():
    atom = AtomicBool(True)

    # Perform compare and exchange operation where the current value matches
    result = atom.compare_exchange(True, False)

    # The swap should be successful, and the previous value should be True
    assert result == (True, True)
    assert atom.load() is False


def test_atomic_bool_compare_exchange_unsuccessful():
    atom = AtomicBool(False)

    # Perform compare and exchange operation where the current value doesn't match
    result = atom.compare_exchange(True, False)

    # The swap should be unsuccessful, and the previous value should be False
    assert result == (False, False)
    assert atom.load() is False


def test_atomic_float_default_constructor():
    atom = AtomicFloat()
    assert atom.load() == 0.0


def test_atomic_float_constructor_with_value():
    atom = AtomicFloat(3.14)
    assert atom.load() == 3.14


def test_atomic_float_store():
    atom = AtomicFloat(1.0)
    atom.store(2.5)
    assert atom.load() == 2.5


def test_atomic_float_add():
    atom = AtomicFloat(1.0)
    previous = atom.add(2.5)
    assert previous == 1.0
    assert atom.load() == 3.5


def test_atomic_float_sub():
    atom = AtomicFloat(5.0)
    previous = atom.sub(2.5)
    assert previous == 5.0
    assert atom.load() == 2.5


def test_atomic_float_swap():
    atom = AtomicFloat(1.0)
    previous = atom.swap(2.0)
    assert previous == 1.0
    assert atom.load() == 2.0


def test_atomic_float_compare_exchange_successful():
    atom = AtomicFloat(1.0)
    result = atom.compare_exchange(1.0, 2.0)
    assert result == (True, 1.0)
    assert atom.load() == 2.0


def test_atomic_float_compare_exchange_unsuccessful():
    atom = AtomicFloat(1.0)
    result = atom.compare_exchange(2.0, 3.0)
    assert result == (False, 1.0)
    assert atom.load() == 1.0


def test_atomic_float_mul():
    atom = AtomicFloat(2.0)
    previous = atom.mul(3.0)
    assert previous == 2.0
    assert atom.load() == 6.0


def test_atomic_float_div_success():
    atom = AtomicFloat(6.0)
    previous = atom.div(2.0)
    assert previous == 6.0
    assert atom.load() == 3.0


def test_atomic_float_div_by_zero():
    atom = AtomicFloat(6.0)
    with pytest.raises(ZeroDivisionError):
        atom.div(0.0)
    # Value should remain unchanged after failed division
    assert atom.load() == 6.0


def test_atomic_float_iadd():
    atom = AtomicFloat(1.0)
    atom += 2.0
    assert atom.load() == 3.0


def test_atomic_float_isub():
    atom = AtomicFloat(3.0)
    atom -= 2.0
    assert atom.load() == 1.0


def test_atomic_float_repr():
    atom = AtomicFloat(3.14)
    assert repr(atom) == "AtomicFloat(3.14)"


def test_atomic_float_str():
    atom = AtomicFloat(3.14)
    assert str(atom) == "3.14"


def test_atomic_float_float_conversion():
    atom = AtomicFloat(3.14)
    assert float(atom) == 3.14


def test_atomic_float_pickle_roundtrip():
    import pickle

    atom = AtomicFloat(3.14)
    data = pickle.dumps(atom)
    restored = pickle.loads(data)
    assert restored.load() == 3.14


def test_atomic_float_nan_handling():
    from math import isnan

    atom = AtomicFloat(float("nan"))
    assert isnan(atom.load())


def test_atomic_float_infinity_handling():
    from math import isinf

    atom = AtomicFloat(float("inf"))
    assert isinf(atom.load())
    assert atom.load() > 0


def test_atomic_float_negative_infinity_handling():
    from math import isinf

    atom = AtomicFloat(float("-inf"))
    assert isinf(atom.load())
    assert atom.load() < 0


def test_atomic_float_thread_safety():
    """Test thread safety by having multiple threads modify the value concurrently."""
    NUM_THREADS = 100
    OPERATIONS_PER_THREAD = 1000

    atomic = AtomicFloat(0.0)
    expected_sum = 0.0  # Track expected final value

    def worker():
        nonlocal expected_sum
        local_sum = 0.0
        for _ in range(OPERATIONS_PER_THREAD):
            value = random.uniform(-1.0, 1.0)
            atomic.add(value)
            local_sum += value
        return local_sum

    # Run operations in multiple threads
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(worker) for _ in range(NUM_THREADS)]
        # Sum up all the changes that should have occurred
        for future in as_completed(futures):
            expected_sum += future.result()

    # Allow a small floating-point error due to accumulated precision differences
    assert abs(atomic.load() - expected_sum) < 1e-10


def test_atomic_float_concurrent_operations():
    """Test different atomic operations happening concurrently."""
    NUM_THREADS = 4
    ITERATIONS = 1000

    atomic = AtomicFloat(1.0)
    operations_completed = threading.Event()

    def adder():
        for _ in range(ITERATIONS):
            atomic.add(1.0)
            time.sleep(0.0001)  # Small sleep to increase chance of thread interleaving

    def subtracter():
        for _ in range(ITERATIONS):
            atomic.sub(1.0)
            time.sleep(0.0001)

    def multiplier():
        for _ in range(ITERATIONS):
            current = atomic.load()
            atomic.compare_exchange(current, current * 2.0)
            time.sleep(0.0001)

    def divider():
        for _ in range(ITERATIONS):
            current = atomic.load()
            if current != 0.0:  # Protect against division by zero
                atomic.compare_exchange(current, current / 2.0)
            time.sleep(0.0001)

    # Start all threads
    threads = [
        threading.Thread(target=adder),
        threading.Thread(target=subtracter),
        threading.Thread(target=multiplier),
        threading.Thread(target=divider),
    ]

    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # The exact final value isn't important - what matters is that
    # we don't get any crashes or race conditions


def test_atomic_float_compare_exchange_race():
    """Test that compare_exchange properly handles race conditions."""
    NUM_COMPETITORS = 10
    atomic = AtomicFloat(0.0)
    winner_count = 0
    barrier = threading.Barrier(NUM_COMPETITORS)

    def compete():
        nonlocal winner_count
        barrier.wait()  # Synchronize all threads to start at the same time
        # Try to be the one to successfully change 0.0 to 1.0
        success, _ = atomic.compare_exchange(0.0, 1.0)
        if success:
            winner_count += 1

    # Create and start threads
    threads = [threading.Thread(target=compete) for _ in range(NUM_COMPETITORS)]
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Exactly one thread should have succeeded
    assert winner_count == 1
    assert atomic.load() == 1.0
