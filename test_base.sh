#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand.cpp -o mand.exe
g++ mand.cpp -o mand_O3.exe -O3 -mavx2

./mand.exe "results/results_base1.txt"
./mand.exe "results/results_base2.txt"
./mand.exe "results/results_base3.txt"
./mand.exe "results/results_base4.txt"
./mand.exe "results/results_base5.txt"
./mand_O3.exe "results/results_base_O3_1.txt"
./mand_O3.exe "results/results_base_O3_2.txt"
./mand_O3.exe "results/results_base_O3_3.txt"
./mand_O3.exe "results/results_base_O3_4.txt"
./mand_O3.exe "results/results_base_O3_5.txt"
