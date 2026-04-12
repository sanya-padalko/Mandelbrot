import matplotlib.pyplot as plt
import numpy as np

def analyze(filename, label):
    data = np.loadtxt(filename)
    data = data[50:] 
    avg = np.mean(data)
    std = np.std(data)
    cpp = avg / (800 * 600)
    print(f"| {label:18}| {int(avg):14,} | {int(std):14,} | {int(np.min(data)):14,} | {cpp:16.2f} |")
    print("-" * 91)
    return avg, std

print("-" * 91)
print(f"| Mandelbrot's type |    Averages    |   Deviations   |    Minimums    | Cycles per pixel |")
print("-" * 91)

files = [('results/results_base.txt', 'Base'),
        ('results/results_base_O3.txt', 'Base + O3'),
        ('results/results_opt.txt', 'Opt (8x8)'),
        ('results/results_opt_O3.txt', 'Opt (8x8) + O3'), 
        ('results/results_avx.txt', 'AVX+FMA'),
        ('results/results_avx_O3.txt', 'AVX+FMA + O3')]

results = [analyze(f, l) for f, l in files]

names = [r[1] for r in files]
avgs = [r[0] for r in results]
stds = [r[1] for r in results]

plt.figure(figsize=(8, 5)) 
plt.bar(names, avgs, width = 0.75, yerr=stds, capsize=28, color=['red', 'blue'], alpha=1)
plt.ylabel('AVG ticks on 950 tests')
plt.title('Mandelbrot\'s Comparison')
#plt.grid(True)
plt.savefig('gisto_mand.svg')
