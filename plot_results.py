import matplotlib.pyplot as plt

base    = [int(x) for x in open('results/results_base.txt')]
base_O3 = [int(x) for x in open('results/results_base_O3.txt')]
opt     = [int(x) for x in open('results/results_opt.txt')]
opt_O3  = [int(x) for x in open('results/results_opt_O3.txt')]
avx     = [int(x) for x in open('results/results_avx.txt')]
avx_O3  = [int(x) for x in open('results/results_avx_O3.txt')]

plt.figure(figsize=(8, 6))
plt.plot(base, label='Base', alpha=0.9)
plt.plot(base_O3, label='Base + O3', alpha=0.9)
plt.plot(opt, label='Opt (8x8)', alpha=0.9)
plt.plot(opt_O3, label='Opt (8x8) + O3', alpha=0.9)
plt.plot(avx, label='AVX + FMA', alpha=0.9)
plt.plot(avx_O3,  label='AVX + FMA + O3', alpha=0.9)

plt.title('Exectuion time of drawing')
plt.xlabel('Iteration\'s index')
plt.ylabel('Ticks')
plt.legend()
plt.grid(True)
plt.savefig('graph_ticks.svg')
