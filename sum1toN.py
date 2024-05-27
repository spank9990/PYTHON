def sum_1_to_N(n):
    if n==0:
        return 0
    ans = n + sum_1_to_N(n-1)
    return ans
print(sum_1_to_N(20))
