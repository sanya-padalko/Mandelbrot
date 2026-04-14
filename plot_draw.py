import matplotlib.pyplot as plt

base    = [int(x) for x in open('results_orig/results_base.txt')]
base_O3 = [int(x) for x in open('results_orig/results_base_O3.txt')]
opt     = [int(x) for x in open('results_orig/results_opt.txt')]
opt_O3  = [int(x) for x in open('results_orig/results_opt_O3.txt')]
avx     = [int(x) for x in open('results_orig/results_avx.txt')]
avx_O3  = [int(x) for x in open('results_orig/results_avx_O3.txt')]

base_no_draw    = [int(x) for x in open('results_no_draw/results_base.txt')]
base_O3_no_draw = [int(x) for x in open('results_no_draw/results_base_O3.txt')]
opt_no_draw     = [int(x) for x in open('results_no_draw/results_opt.txt')]
opt_O3_no_draw  = [int(x) for x in open('results_no_draw/results_opt_O3.txt')]
avx_no_draw     = [int(x) for x in open('results_no_draw/results_avx.txt')]
avx_O3_no_draw  = [int(x) for x in open('results_no_draw/results_avx_O3.txt')]

plt.figure(figsize=(8, 6))
plt.plot(base, label='Base', alpha=0.9, color='red')
plt.plot(base_O3, label='Base + O3', alpha=0.9, color='red')
plt.plot(opt, label='Opt (8x8)', alpha=0.9, color='red')
plt.plot(opt_O3, label='Opt (8x8) + O3', alpha=0.9, color='red')
plt.plot(avx, label='AVX + FMA', alpha=0.9, color='red')
plt.plot(avx_O3,  label='AVX + FMA + O3', alpha=0.9, color='red')

plt.plot(base_no_draw, label='Base', alpha=0.9, color='blue')
plt.plot(base_O3_no_draw, label='Base + O3', alpha=0.9, color='blue')
plt.plot(opt_no_draw, label='Opt (8x8)', alpha=0.9, color='blue')
plt.plot(opt_O3_no_draw, label='Opt (8x8) + O3', alpha=0.9, color='blue')
plt.plot(avx_no_draw, label='AVX + FMA', alpha=0.9, color='blue')
plt.plot(avx_O3_no_draw,  label='AVX + FMA + O3', alpha=0.9, color='blue')

plt.title('Exectuion time of drawing')
plt.xlabel('Iteration\'s index')
plt.ylabel('Ticks')
plt.legend()
plt.grid(True)
plt.savefig('draw_comp.svg')
