def method1(arr):
    ret = [xpos for xpos in arr if xpos != 0]
    return ret + [0 for xpos in range(len(arr)-len(ret))]
def method2(arr):
    pass
def method3(arr):
    pass
arr = [1,23,0,0,1,0,4,1]
print(method1(arr))

