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
    s_avg.append(avg)

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
print(f"Base avg: {int(avg)} ticks")
s_avg = []
res_base = []
print()


for i in range(5):
    file_name = file1 + '_O3_' + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    s_avg.append(avg)

s_avg.sort()
avg = sum(s_avg[1:4]) / 3
std_s = 0
for i in range(5):
    std_s += (s_avg[i] - avg) * (s_avg[i] - avg)

std_s = sqrt(std_s / 5)

for i in range(5):
    print(f"Base O3 #{i + 1}: {int(s_avg[i])} ticks")

print()
print(f"Relative error: {(std_s / avg * 100):.2}%")
print(f"Base O3 avg: {int(avg)} ticks")
s_avg = []
res_base = []
print()

for i in range(5):
    file_name = file2 + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    s_avg.append(avg)

s_avg.sort()
avg = sum(s_avg[1:4]) / 3
std_s = 0
for i in range(5):
    std_s += (s_avg[i] - avg) * (s_avg[i] - avg)

std_s = sqrt(std_s / 5)

for i in range(5):
    print(f"Opt (8x8) #{i + 1}: {int(s_avg[i])} ticks")

print()
print(f"Relative error: {(std_s / avg * 100):.2}%")
print(f"Opt (8x8) avg: {int(avg)} ticks")
s_avg = []
print()



for i in range(5):
    file_name = file2 + '_O3_' + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    s_avg.append(avg)

s_avg.sort()
avg = sum(s_avg[1:4]) / 3
std_s = 0
for i in range(5):
    std_s += (s_avg[i] - avg) * (s_avg[i] - avg)

std_s = sqrt(std_s / 5)

for i in range(5):
    print(f"Opt (8x8) O3 #{i + 1}: {int(s_avg[i])} ticks")

print()
print(f"Relative error: {(std_s / avg * 100):.2}%")
print(f"Opt (8x8) O3 avg: {int(avg)} ticks")
s_avg = []
res_base = []
print()



for i in range(5):
    file_name = file3 + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    s_avg.append(avg)

s_avg.sort()
avg = sum(s_avg[1:4]) / 3
std_s = 0
for i in range(5):
    std_s += (s_avg[i] - avg) * (s_avg[i] - avg)

std_s = sqrt(std_s / 5)

for i in range(5):
    print(f"AVX #{i + 1}: {int(s_avg[i])} ticks")

print()
print(f"Relative error: {(std_s / avg * 100):.2}%")
print(f"AVX avg: {int(avg)} ticks")
s_avg = []
res_base = []
print()



for i in range(5):
    file_name = file3 + '_O3_' + str(i + 1) + '.txt'
    res_base.append(analyze(file_name))
    avg = res_base[i][0]
    s_avg.append(avg)

s_avg.sort()
avg = sum(s_avg[1:4]) / 3
std_s = 0
for i in range(5):
    std_s += (s_avg[i] - avg) * (s_avg[i] - avg)

std_s = sqrt(std_s / 5)

for i in range(5):
    print(f"AVX O3 #{i + 1}: {int(s_avg[i])} ticks")

print()
print(f"Relative error: {(std_s / avg * 100):.2}%")
print(f"AVX O3 avg: {int(avg)} ticks")
s_avg = []
res_base = []
print()

