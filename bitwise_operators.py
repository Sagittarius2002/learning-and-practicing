a, b = 6, 3   # binary: a=0110, b=0011

print(a & b)   # 2  (0010)
print(a | b)   # 7  (0111)
print(a ^ b)   # 5  (0101)
print(~a)      # -7 (two's complement of 6)
print(a << 1)  # 12 (1100)
print(a >> 1)  # 3  (0011)