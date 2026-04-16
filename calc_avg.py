import numpy as np
from math import sqrt

def analyze(filename):
    data = np.loadtxt(filename)
    data = data[50:] 
    avg = np.mean(data)
    std = np.std(data)
    return avg, std

def print_result(filename, label):
    res = []
    s_avg = []
    for i in range(5):
        file_name = filename + str(i + 1) + '.txt'
        res.append(analyze(file_name))
        s_avg.append(res[i][0])

    s_avg.sort()
    avg = sum(s_avg[1:4]) / 3
    std_s = 0
    for i in range(5):
        std_s += (s_avg[i] - avg) * (s_avg[i] - avg)
    std_s = sqrt(std_s / 5)
    for i in range(5):
        print(f"Base #{i + 1}: {int(s_avg[i])} ticks")

    print()
    print(f"Relative error: {(std_s / avg * 100):.2}%")
    print(f"{label}: {int(avg)} ticks")
    s_avg = []
    res_base = []
    print()

print_result('results/results_base', 'Base avg')
print_result('results/results_base_O3_', 'Base O3 avg')
print_result('results/results_opt', 'Opt avg')
print_result('results/results_opt_O3_', 'Opt O3 avg')
print_result('results/results_avx', 'AVX avg')
print_result('results/results_avx_O3_', 'AVX O3 avg')
