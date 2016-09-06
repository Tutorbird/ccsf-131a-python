#!/usr/local/bin/python3
# Creator: NESTOR ALVAREZ
# 20160718

import helpers

#See if all the methods are accessible through the main method
print(helpers.__main__())


print("Testing individually...")
#See if they still work individually
print(helpers.area(10))
print(helpers.circ(10))
print(helpers.c2f(3))
print(helpers.f2c(3))
print("Should be 4 lines of output")
