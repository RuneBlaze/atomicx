import threading
from atomicx import AtomicInt, AtomicBool


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