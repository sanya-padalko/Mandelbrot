#!/bin/bash

g++ mand256_1.cpp -o mand256_1.exe -mavx2 -mfma -O3
g++ mand256_2.cpp -o mand256_2.exe -mavx2 -mfma -O3

./mand256_1 "result256_1.txt"
./mand256_2 "result256_2.txt"

python3 plot2.py