import matplotlib.pyplot as plt

circle = plt.Circle((0.5, 0.5), 0.2, color='blue')

fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_ylabel('height')
ax.set_xlabel('length')
ax.set_title('Draw a circle')

<<<<<<< HEAD
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


=======
>>>>>>> ad4f4202ec6ada10440ddb74fc8f0a53501facfa
fig.savefig('plotcircles.png')
