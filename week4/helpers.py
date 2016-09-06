#!/usr/local/bin/python3
# Nestor Alvarez
# helpers.py
# Handles some routine CGI chores
# 201607018

def __main__():
    print("#" * 28,"\n", "Testing...1, 2, 3...testing!\n", "#" * 28, "\n", sep="")
    # code to test area() and circ()
    radius = 10
    print("A circle with a radius of {} has a circumference of {:.2f} \
units and an area of {:.2f} square units.".format(radius, circ(radius), area(radius)))
    print(c2f(30))
    print(f2c(30))

pi = 3.14159
def area(r):
    ##area(r): return the area of a circle with radius r.
    global pi
    return(pi * r * r)

def circ(r):
    global pi
    return(2 * pi * r)
def f2c(num):
    C2F_CONSTANT = 1.8
    celsius = round(((num - 32) / C2F_CONSTANT))
    return True
def c2f(num):
    C2F_CONSTANT = 1.8
    fahrenheit = (num * C2F_CONSTANT + 32)
    return True

if __name__ == '__main__':
      __main__()

