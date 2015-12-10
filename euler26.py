#!/usr/bin/python

fp = open("names.txt", "r")

file = fp.read()
names = sorted(file.split(','))

totsum = 0

for i in range(len(names)):
#for i in range(10):
    names[i] = names[i].strip('"')
    sum = 0
    for j in range( len(names[i]) ):
        sum += ord (names[i][j]) - 64
    totsum += sum * (i+1)
#    print i, names[i], sum

print totsum
