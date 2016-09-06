#!/usr/local/bin/python3
# NAME: Nestor Alvarez
# FILE: columns.py
# DATE: Week 2

# re is the regular expression module; we have to import it.
import re

text = open('/users/dputnam/oliver.txt').read().lower()

words = re.split("[^\w'-]+", text)
words = [i for i in words if i != '' ]

first = words[0:100]
second = words[100: 2724]


count = 0
for i in range(0, 17):
    for i in range(0, 6):
        print("{0:>16}".format(first[count]), end= ' ')
        count += 1
        if count == 100:
            break
    print()

print("\nThere are %s words in total" % len(words))
print("There are %s unique words in the first sequence" % len(set(first)))
print("They are: ")
print(set(first))
print("There are %s unique words in the second sequence" % len(set(second)))
print("They are: ")
print(set(second))
print("Overall, there are %s unique words" % len(set(second).union(set(first))))
print("They are: ")
print(set(second).union(set(first)))
xor_count = len(set(second).symmetric_difference(set(first)))
print("There are %s exclusively, unique words from both sets" % xor_count)

first_only = []

for x in first:
    if x not in second:
        first_only.append(x)

first_only = list(set(first_only))
first_only.sort()
print("There are %s words in the first set not in the second set" % len(first_only))
print("They are: ")
print(first_only)

second_only = []
        
for x in second:
    if x not in first:
        second_only.append(x)

second_only = list(set(second_only))
second_only.sort()
print("There are %s words in the second set not in the first set" % len(second_only))
print("They are: ")
print(second_only)
