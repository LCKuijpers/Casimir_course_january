import numpy as np

r = 2

"calculation of the circumvent of the circle"
def cv(r):
    return 2 * r *np.pi

print('the circumvent of the circle is', cv(r))


"calculation of the surface area of the circle"
def surf(r):
    return 2 ** r *np.pi

print('the surface area of the circle is', surf(r))
