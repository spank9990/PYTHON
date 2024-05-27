def power(a,b):

    #base case
    if b==0:
        return 1
    
    #recursive case
    ans = a*power(a,b-1)
    return ans

print(power(2,3))
