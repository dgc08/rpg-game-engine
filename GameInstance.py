class __GameInstance:
    _obj = None

def GameInstance(arg=None):
    if arg != None:
        __GameInstance._obj = arg
    else:
        return  __GameInstance._obj