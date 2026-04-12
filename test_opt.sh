#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand_8.cpp -o mand_8.exe
g++ mand_8.cpp -o mand_8_O3.exe -O3

./mand_8.exe "results/results_opt.txt"
./mand_8_O3.exe "results/results_opt_O3.txt"