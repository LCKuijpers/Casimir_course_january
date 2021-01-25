print('commit test')

print('successful')


import test
print(test.cv(test.r))

import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 0.2, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
circle3 = plt.Circle((1, 1), 0.2, color='g')

fig, ax = plt.subplots()

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.set_xlabel('nanometers')
ax.set_ylabel('nothing')


fig.savefig('plotcircles.png')
