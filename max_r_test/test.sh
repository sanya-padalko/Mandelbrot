#!/bin/bash

g++ mand1.cpp -o mand1.exe
g++ mand2.cpp -o mand2.exe

./mand1 "result1.txt"
./mand2 "result2.txt"

python3 plot.py