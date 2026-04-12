#!/bin/bash

./test_base.sh
./test_opt.sh
./test_avx.sh

python3 calc_graph.py
python3 plot_results.py