#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
owners = ['Farrah', 'Fred', 'Felicia']
fruit_names_and_colors = (
    ('apples', 'red'),
    ('bananas', 'yellow'),
    ('oranges', '#ff8000'),
    ('peaches', '#ffe5b4')
)

bottom_spacing = np.zeros(fruit.shape[1])
for i in range(len(fruit)):
    plt.bar(
        owners,
        fruit[i],
        bottom=bottom_spacing,
        width=0.5,
        label=fruit_names_and_colors[i][0],
        color=fruit_names_and_colors[i][1],
    )
    bottom_spacing += fruit[i]

plt.ylim(0, 80)
plt.yticks(np.arange(0, 90, 10))
plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.legend()
plt.show()