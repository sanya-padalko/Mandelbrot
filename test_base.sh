#!/bin/bash

if [ ! -d "results" ]; then
    mkdir "results"
fi;

g++ mand.cpp -o mand.exe
g++ mand.cpp -o mand_O3.exe -O3

./mand.exe "results/results_base.txt"
./mand_O3.exe "results/results_base_O3.txt"
