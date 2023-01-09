#!/usr/bin/python3
def lookup(obj):
    #keyList = list(obj.__dict__.keys())
    #print(sorted(keyList))
    #return (sorted(keyList))

    if obj and type(obj) is type:
        return dir(obj)
    else:
        raise TypeError("obj must be a class or subclass")
