import matplotlib.pyplot as plt

base1    = [int(x) for x in open('result1.txt')]
base2    = [int(x) for x in open('result2.txt')]

print(sum(base1[50:]) / len(base1[50:]))
print(sum(base2[50:]) / len(base2[50:]))

plt.figure(figsize=(8, 6))
plt.plot(base1, label='With const', alpha=0.9)
plt.plot(base2, label='Without const', alpha=0.9)

plt.ylim(int(2e8), int(8e8))
plt.title('Exectuion time of drawing')
plt.xlabel('Iteration\'s index')
plt.ylabel('Ticks')
plt.legend()
plt.grid(True)
plt.savefig('plot.svg')
