#!/usr/bin/env python

def read_name_set(sam1,sam2):
  s = set(l.split()[0] for l in sam1 if l[0] != "@")
  s.intersection_update(l.split()[0] for l in sam2 if l[0] != "@")
  return s

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("sam_1", type=argparse.FileType("r"))
parser.add_argument("sam_2", type=argparse.FileType("r"))
args = parser.parse_args()

s = read_name_set(args.sam_1, args.sam_2)
args.sam_1.seek(0)
for l in args.sam_1:
  if l [0] == "@" or l.split()[0] in s:
    print l.strip()
