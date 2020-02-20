def subtractProductAndSum(num):
    x = []
    while num!=0:
        x.append(num%10)
        num //= 10
    product = 1
    for i in x:
        product = product * i
    s = sum(x)
    return (product-s) 
    
print(subtractProductAndSum(4421))



    