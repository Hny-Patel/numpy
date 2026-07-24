"""
NumPy Basics
------------

This script demonstrates the fundamentals of NumPy, including:

1. Creating 1D and 2D arrays
2. Array properties (shape, dimensions, item size)
3. Indexing and updating elements
4. Sorting arrays
5. Creating arrays using zeros, ones, arange, and linspace
6. Reshaping and flattening arrays
7. Aggregate functions (min, max, sum)
8. Iterating over arrays
9. Mathematical functions (sqrt and standard deviation)

Author: Hiren Patel
"""

import numpy as np


print("=" * 60)
print("1. ARRAY CREATION")
print("=" * 60)

# Revenue for Quarter 1 (1D Array)
quarter1_revenue = np.array([10, 12, 14])

print("Quarter 1 Revenue:")
print(quarter1_revenue)

print("Number of Dimensions:", quarter1_revenue.ndim)

# Revenue for multiple quarters (2D Array)
quarter_revenue = np.array([
    [10, 12, 14],
    [14, 23, 14]
])

print("\nQuarter Revenue:")
print(quarter_revenue)

print("Number of Dimensions:", quarter_revenue.ndim)


print("\n" + "=" * 60)
print("2. INDEXING AND UPDATING")
print("=" * 60)

# Access an element
print("Revenue of Quarter 2, Month 1:", quarter_revenue[1, 0])

# Update an incorrect value
quarter_revenue[1, 2] = 24

print("\nUpdated Revenue:")
print(quarter_revenue)


print("\n" + "=" * 60)
print("3. ARRAY PROPERTIES")
print("=" * 60)

print("Item Size:", quarter_revenue.itemsize, "bytes")

# Create array with float64 datatype
quarter_revenue_float = np.array(
    [[10, 12, 14],
     [14, 23, 14]],
    dtype=np.float64
)

print("Float64 Item Size:", quarter_revenue_float.itemsize, "bytes")

print("Shape:", quarter_revenue_float.shape)

print("Data Type:", quarter_revenue_float.dtype)


print("\n" + "=" * 60)
print("4. SORTING")
print("=" * 60)

print("Row-wise Sorting:")
print(np.sort(quarter_revenue_float))

print("\nComplete Array Sorting:")
print(np.sort(quarter_revenue_float, axis=None))


print("\n" + "=" * 60)
print("5. CREATING ARRAYS")
print("=" * 60)

print("Zeros Array:")
print(np.zeros((3, 2)))

print("\nOnes Array:")
print(np.ones((3, 2)))

print("\nUsing arange():")
print(np.arange(10, 20, 2))

print("\nUsing linspace():")
print(np.linspace(1, 4, 5))


print("\n" + "=" * 60)
print("6. RESHAPING")
print("=" * 60)

print("Flattened Array:")
print(quarter_revenue.flatten())

print("\nReshaped Array:")
print(quarter_revenue.reshape(2, 3))


print("\n" + "=" * 60)
print("7. AGGREGATE FUNCTIONS")
print("=" * 60)

print("Minimum Revenue:", quarter_revenue.min())
print("Maximum Revenue:", quarter_revenue.max())

# Total revenue for each quarter
print("\nTotal Revenue of Each Quarter:")
print(quarter_revenue.sum(axis=1))

# Combined monthly revenue across all quarters
print("\nMonthly Revenue Across All Quarters:")
print(quarter_revenue.sum(axis=0))


print("\n" + "=" * 60)
print("8. ITERATING OVER ROWS")
print("=" * 60)

for index, row in enumerate(quarter_revenue, start=1):
    print(f"Quarter {index}: {row}")


print("\n" + "=" * 60)
print("9. MATHEMATICAL FUNCTIONS")
print("=" * 60)

square_numbers = np.array([1, 4, 16])

print("Square Numbers:")
print(square_numbers)

print("\nSquare Root:")
print(np.sqrt(square_numbers))

print("\nStandard Deviation:")
print(np.std(square_numbers))