#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand_8.cpp -o mand_8.exe
g++ mand_8.cpp -o mand_8_O3.exe -O3 -mavx2

./mand_8.exe "results/results_opt1.txt"
./mand_8.exe "results/results_opt2.txt"
./mand_8.exe "results/results_opt3.txt"
./mand_8.exe "results/results_opt4.txt"
./mand_8.exe "results/results_opt5.txt"
./mand_8_O3.exe "results/results_opt_O3_1.txt"
./mand_8_O3.exe "results/results_opt_O3_2.txt"
./mand_8_O3.exe "results/results_opt_O3_3.txt"
./mand_8_O3.exe "results/results_opt_O3_4.txt"
./mand_8_O3.exe "results/results_opt_O3_5.txt"