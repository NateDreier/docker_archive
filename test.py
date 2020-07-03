#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('infile')
args = parser.parse_args()
with open(args.infile) as file:
    for line in file:
        print(line)

