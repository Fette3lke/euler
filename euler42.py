#!/usr/bin/python

fp = open("words.txt", "r")

file = fp.read()
words = file.split(',')

nt = 0

triangle = set([i*(i+1)/2 for i in range(1,21)])


for i in range(len(words)):
#for i in range(10):
    words[i] = words[i].strip('"')
    sum = 0
    for j in range( len(words[i]) ):
        sum += ord (words[i][j]) - 64
    if sum in triangle:
        nt += 1
#    print i, names[i], sum

print nt
