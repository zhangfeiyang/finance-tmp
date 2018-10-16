#!/usr/bin/python3

file0 = open('index0','r')
file = open('index','r')

indexs = file.read().split()
index0s = file0.read().split()

for index0 in index0s:
    if not index0 in indexs:
        indexs.append(index0)

for index in indexs:
    print(index)
