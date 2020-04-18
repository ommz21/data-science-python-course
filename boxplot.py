# Boxplot - diagrama de caixa
import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    num_alea = random.randint(0, 1000000)
    vetor.append(num_alea)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()