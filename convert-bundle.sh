#!/bin/bash
set -euo pipefail

curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz > lab3-bundle.tar.gz

tar -xvzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

NUM_ROWS=$(( $(wc -l < cleaned.csv) - 1))

echo $NUM_ROWS

tar -czvf converted-archive.tar.gz cleaned.csv