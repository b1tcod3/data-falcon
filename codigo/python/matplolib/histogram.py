from collections import Counter                   # not loaded by default
from matplotlib import pyplot as plt

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10

histogram = Counter(decile(grade) for grade in grades) # shift each bar to the left by 4

plt.bar([x - 4 for x in histogram.keys()], # give each bar its correct height
histogram.values(),                         # give each bar a width of 8
8)

# y-axis from 0 to 5
plt.axis([-5, 105, 0, 5]) # x-axis from -5 to 105,

plt.xticks([10 * i for i in range(11)]) #x-axis labels at 0, 10, ..., 100

plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()