# Big O - Tips

## Overview
Big O notation describes the time complexity of algorithms, showing how their performance scales with input size. These tips will help you remember the key complexities.

## Big O's

### O(1) - Constant
No loops

### O(log N) - Logarithmic
Usually searching algorithms have log n if they are sorted (Binary Search)

### O(n) - Linear
For loops, while loops through n items

### O(n log(n)) - Log Linear
Usually sorting operations

### O(n^2) - Quadratic
Every element in a collection needs to be compared to ever other element. Two nested loops

### O(2^n) - Exponential 
Recursive algorithms that solves a problem of size N

### O(n!) - Factorial
You are adding a loop for every element

## Big O Table

| Big O   | Name          | Description                                    |
|---------|---------------|------------------------------------------------|
| O(1)    | Constant      | Statement, one line of code                    |
| O(log n)| Logarithmic   | Divide and conquer (binary search)             |
| O(n)    | Linear        | Loop                                           |
| O(n log n) | Linearithmic | Effective sorting algorithms                   |
| O(n^2)  | Quadratic     | Double loop                                    |
| O(n^3)  | Cubic         | Triple loop                                    |
| O(2^n)  | Exponential   | Complex full search                            |

## Sorting Algorithms

| Sorting Algorithm | Space Complexity | Best Case Time Complexity | Worst Case Time Complexity |
|-------------------|------------------|---------------------------|----------------------------|
| **Insertion Sort** | O(1)             | O(n)                      | O(n²)                      |
| **Selection Sort** | O(1)             | O(n²)                     | O(n²)                      |
| **Bubble Sort**    | O(1)             | O(n)                      | O(n²)                      |
| **Mergesort**      | O(n)             | O(n log n)                | O(n log n)                 |
| **Quicksort**      | O(log n)         | O(n log n)                | O(n²)                      |
| **Heapsort**       | O(1)             | O(n log n)                | O(n log n)                 |

## Common Data Structure Operations

| Data Structure        | Access | Search | Insertion | Deletion | Space Complexity |
|-----------------------|--------|--------|-----------|----------|------------------|
| **Array**             | O(1)   | O(n)   | O(n)      | O(n)     | O(n)             |
| **Stack**             | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| **Queue**             | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| **Singly-Linked List**| O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| **Doubly-Linked List**| O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| **Hash Table**        | N/A    | O(n)   | O(n)      | O(n)     | O(n)             |


