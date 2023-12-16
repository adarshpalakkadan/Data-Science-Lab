import numpy as np
import matplotlib.pyplot as plt

data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':7.7,'C++':6.7}
color=("red","yellow","maroon","green","black","cyan")

courses = list(data.keys())
values = list(data.values())


plt.bar(courses, values, color =color)

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()

