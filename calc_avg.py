import numpy as np
from math import sqrt

def analyze(filename):
    data = np.loadtxt(filename)
    data = data[50:] 
    avg = np.mean(data)
    std = np.std(data)
    return avg, std

file1 = 'results/results_base'
file2 = 'results/results_opt'
file3 = 'results/results_avx'

res_base = []
res_opt  = []
res_avx  = []
res_base_O3 = []
res_opt_O3  = []
res_avx_O3  = []

s_avg = []

for i in range(5):
    file_name = file1 + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    std = res_base[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"Base #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"Base avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()


for i in range(5):
    file_name = file1 + '_O3_' + str(i + 1) + '.txt'
    res_base_O3.append(analyze(file_name))
    avg = res_base_O3[i][0]
    std = res_base_O3[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"Base O3 #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"Base O3 avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()


for i in range(5):
    file_name = file2 + str(i + 1) + '.txt'
    res_opt.append(analyze(file_name))
    avg = res_opt[i][0]
    std = res_opt[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"Opt #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"Opt avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()



for i in range(5):
    file_name = file2 + '_O3_' + str(i + 1) + '.txt'
    res_opt_O3.append(analyze(file_name))
    avg = res_opt_O3[i][0]
    std = res_opt_O3[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"Opt O3 #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"Opt O3 avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()



for i in range(5):
    file_name = file3 + str(i + 1) + '.txt'
    res_avx.append(analyze(file_name))
    avg = res_avx[i][0]
    std = res_avx[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"AVX #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"AVX avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()



for i in range(5):
    file_name = file3 + '_O3_' + str(i + 1) + '.txt'
    res_avx_O3.append(analyze(file_name))
    avg = res_avx_O3[i][0]
    std = res_avx_O3[i][1]
    std = 2.78 * sqrt(std / 4) / sqrt(5)

    print(f"AVX O3 #{i + 1}: {int(avg)} +- {int(std)} ticks")
    s_avg.append(avg)

print()
print(f"AVX O3 avg: {int((sum(s_avg) - min(s_avg) - max(s_avg)) / 3)}")
s_avg = []
print()

