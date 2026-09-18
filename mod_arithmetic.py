def mod_add(a, b, q):
    return (a + b) % q

def mod_mul(a, b, q):
    return (a * b) % q

# 测试
q = 11
print("(12 + 7) mod 11 =", mod_add(12,7,q))
print("(6 * 4) mod 11 =", mod_mul(6,4,q))
print("17 mod 5 =", 17 % 5)
