import numpy as np

data = list(range(20, 100, 5))
print(data)

q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.55)
q3 = np.quantile(data, 0.75)

print("Quartile 1: ", q1)
print("Quartile 2: ", q2)
print("Quartile 3: ", q3)


def quartile_deviation(a, b):
    return (b - a) / 2


print(quartile_deviation(q1, q3))
