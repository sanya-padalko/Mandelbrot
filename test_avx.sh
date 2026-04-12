#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand_float256.cpp -o mand_float256.exe -mavx2 -mfma
g++ mand_float256.cpp -o mand_float256_O3.exe -mavx2 -mfma -O3

./mand_float256.exe "results/results_avx.txt"
./mand_float256_O3.exe "results/results_avx_O3.txt"