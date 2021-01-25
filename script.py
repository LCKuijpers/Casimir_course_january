import matplotlib.pyplot as plt

circle = plt.Circle((0.5, 0.5), 0.2, color='blue')

fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_ylabel('height')
ax.set_xlabel('length')
ax.set_title('Draw a circle')

fig.savefig('plotcircles.png')
