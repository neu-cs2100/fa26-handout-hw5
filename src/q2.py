"""HW5 Question 2

Please read the provided Building class below.

Please write a function takes a list of Building instances and returns the sum of the
number of floors in the last n Buildings in the list, where n is specified as an argument 
to the function. If n is longer than the list of buildings, consider all buildings in the list.
If n is zero, the function should return 0.

Example usage:
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 2) -> 7
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 1) -> 2
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 3) -> 10
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 0) -> 0
"""
