import numpy as np

r = 2
def cv(r):
    return 2 * r *np.pi

print('the circumvent of the circle is', cv(r), 'nanometer')

def surf(r):
    return 2 ** r *np.pi

print('the surface area of the circle is', surf(r))
