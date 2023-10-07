from icecream import ic

def myfunction(v):
    if v % 2 == 0:
        ic()
        return True
    else:
        return False


print(myfunction(10))