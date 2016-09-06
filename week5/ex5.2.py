#!/usr/local/bin/python3
# NAME: NESTOR ALVAREZ
# FILE: ex5.2.py
# DATE: 20160725
# DESC: Exceptions

def __main__():
    am_i_true_or_false = [ True, None, False, "True", 0, "", 8, "False", "True", "0.0" ]
    for i in range(0, (len(am_i_true_or_false))):
        
        try:
            testvar = am_i_true_or_false[i]
            testresult = TrueOrFalse(testvar)
            if testresult == True:
                print("{} is {}.".format(testvar, testresult))
            else:
                raise(OhNoNotTrueError("{} is false".format(testvar)))
        except OhNoNotTrueError as e:
            print(e)

class OhNoNotTrueError(Exception):
    pass

def TrueOrFalse(var):
    return bool(var);

if __name__ == '__main__':
    __main__()
