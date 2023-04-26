# 최대 공약수 최소 공배수

def getGcd(a, b):
    while b != 0:
        a, b = b, a%b

    return a

print(getGcd(24, 16))
print(getGcd(16, 24))

# 최소공배수
print(24*16//getGcd(24, 16))