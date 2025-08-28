import numpy as np

coefficients = [2, -8, 6, -4, 2]

p = np.poly1d(coefficients)
print(f"поліном \n{coefficients}")

roots = np.roots(coefficients)
print(f"\nкорені полінома \n{roots}")

p1 = p.deriv()
print(f"\nперша похідна, \n{p1}")

p2 = p1.deriv()
print(f"\nдруга похідна, \n{p2}")

n = 50
value_at_50 = p(n)
print(f"\nO(50) = \n{value_at_50}")