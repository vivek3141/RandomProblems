def method1(arr):
    ret = [x for x in arr if x != 0]
    return ret + [0 for x in range(len(arr)-len(ret))]
def method2(arr):
    pass
def method3(arr):
    pass
arr = [1,23,0,0,1,0,4,1]
print(method1(arr))