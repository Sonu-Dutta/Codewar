def count_sheep(n):
# method1
    # result = ""
    # for i in range(0,n):
    #     result+=( str(i+1) + " sheep...")
    # return result
    
# method2
    # return "".join(str(i) + " sheep..." for i in range(1, n + 1))
    
# method3
     return "".join("{} sheep...".format(i) for i in range(1, n+1))

print(count_sheep(6))