# coding=utf-8
def gcd( a, b):     # 欧几里得算法 gcd(a, b) == gcd(b, a mod b) 不妨设 a>b
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def gcd(a,b):         # 递归调用
    if a%b ==0:
        return b
    return gcd(b, a%b)

print gcd(25,15)      #输出为5