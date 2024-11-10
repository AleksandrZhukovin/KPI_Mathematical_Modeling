"""
Варіант 6
z = 4*x1 + 2*x2 (max)
{-x1 + 2*x2 <= 6
{ x1 + x2 <= 9
{ 3*x1 - x2 <= 15
{ x1 >= 0, x2 >= 0
"""

from scipy.optimize import linprog


coefs = [1, -3]
A = [
    [1, 2],
    [-1, 1],
    [1, 1],
]
A0 = [4, -1, 8]

res = linprog(coefs, A_ub=A, b_ub=A0,  bounds=[(0, None), (0, None)], method='simplex')
x1 = res.x[0]
x2 = res.x[1]
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"z = {x1*4 + x2*2}")
