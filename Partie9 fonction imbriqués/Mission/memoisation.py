import time


def test_time(fct1,fct2,n):
    
    t0 = time.clock()
    result = fct1(n)
    t1 = time.clock()
    print("fct1({0}) = {1}, ({2:.10f} secs)".format(n, result, t1-t0))
    
    t2 = time.clock()
    result = fct2(n)
    t3 = time.clock()
    print("fct2({0}) = {1}, ({2:.10f} secs)".format(n, result, t3-t2))
    

dict_mapping={} 


def memoisation(fct,n):
    if fct not in dict_mapping:
         dict_mapping[fct]={}
    if n in dict_mapping[fct]:
         return dict_mapping[fct][n]
    dict_mapping[fct][n] = fct(n)
    return dict_mapping[fct][n]

def fib_mem(n):
    dict_mapping[fib_mem]={}
    dict_mapping[fib_mem][0] = 0
    dict_mapping[fib_mem][1] = 1
    
    if n not in dict_mapping[fib_mem]:
        dict_mapping[fib_mem][n] = memoisation(fib_mem,n-1) + memoisation(fib_mem,n-2)
    return dict_mapping[fib_mem][n]
    
    
print(fib_mem(200))
    
    