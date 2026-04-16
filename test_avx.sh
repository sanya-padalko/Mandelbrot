#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand_float256.cpp -o mand_float256.exe -mavx2 -mfma
g++ mand_float256.cpp -o mand_float256_O3.exe -mavx2 -mfma -O3

./mand_float256.exe "results/results_avx1.txt"
./mand_float256.exe "results/results_avx2.txt"
./mand_float256.exe "results/results_avx3.txt"
./mand_float256.exe "results/results_avx4.txt"
./mand_float256.exe "results/results_avx5.txt"
./mand_float256_O3.exe "results/results_avx_O3_1.txt"
./mand_float256_O3.exe "results/results_avx_O3_2.txt"
./mand_float256_O3.exe "results/results_avx_O3_3.txt"
./mand_float256_O3.exe "results/results_avx_O3_4.txt"
./mand_float256_O3.exe "results/results_avx_O3_5.txt"