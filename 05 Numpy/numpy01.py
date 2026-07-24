"""
NumPy vs Python List
--------------------

This script compares Python lists and NumPy arrays in terms of:

1. Memory consumption
2. Execution speed
3. Ease of performing element-wise operations

Author: Hiren Patel
"""

import sys
import time
import numpy as np


def compare_memory() -> None:
    """
    Compare memory usage between a Python list and a NumPy array.
    """

    print("=" * 60)
    print("MEMORY COMPARISON")
    print("=" * 60)

    # Create a Python list with 100 integers
    python_list = list(range(100))

    # Display the last 5 elements
    print(f"Python List (last 5 elements): {python_list[95:]}")

    # Approximate memory usage
    # Note:
    # sys.getsizeof(python_list[0]) returns the size of a single integer object.
    # Multiplying by the number of elements provides only an approximation and
    # does NOT include the list object's internal overhead.
    approx_list_memory = sys.getsizeof(python_list[0]) * len(python_list)

    print(f"Approximate memory used by list elements: {approx_list_memory} bytes")

    # Create a NumPy array
    numpy_array = np.arange(100)

    print(f"NumPy Array (last 5 elements): {numpy_array[95:]}")

    # Total bytes occupied by the NumPy array
    print(f"Memory used by NumPy array: {numpy_array.nbytes} bytes")


def compare_performance(size: int = 1_000_000) -> None:
    """
    Compare execution time for element-wise addition.

    Parameters
    ----------
    size : int
        Number of elements in each collection.
    """

    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    # -------------------------
    # Python List
    # -------------------------
    list_1 = list(range(size))
    list_2 = list(range(size))

    start = time.time()

    result_list = [x + y for x, y in zip(list_1, list_2)]

    end = time.time()

    print(f"Python List Time : {end - start:.6f} seconds")

    # Prevent optimization warning
    del result_list

    # -------------------------
    # NumPy Array
    # -------------------------
    array_1 = np.arange(size)
    array_2 = np.arange(size)

    start = time.time()

    result_array = array_1 + array_2

    end = time.time()

    print(f"NumPy Array Time : {end - start:.6f} seconds")

    del result_array


def demonstrate_vectorization() -> None:
    """
    Demonstrate NumPy's vectorized operations.
    """

    print("\n" + "=" * 60)
    print("VECTORIZED OPERATIONS")
    print("=" * 60)

    array_1 = np.arange(5)
    array_2 = np.arange(5)

    result = array_1 + array_2

    print(f"Array 1 : {array_1}")
    print(f"Array 2 : {array_2}")
    print(f"Result  : {result}")


def main() -> None:
    """
    Entry point of the program.
    """

    compare_memory()
    compare_performance()
    demonstrate_vectorization()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print("Python List")
    print("- Can store heterogeneous data types.")
    print("- Stores references to objects.")
    print("- Higher memory overhead.")
    print("- Slower for numerical computations.")

    print("\nNumPy Array")
    print("- Stores homogeneous data types.")
    print("- Uses contiguous memory allocation.")
    print("- Lower memory consumption.")
    print("- Faster due to vectorized operations implemented in C.")
    print("- Supports simple and efficient mathematical operations.")


if __name__ == "__main__":
    main()