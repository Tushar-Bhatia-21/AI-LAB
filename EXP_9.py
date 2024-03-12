def xor_gate(x, y):
    if x == y:
        return 0
    else:
        return 1

# Test cases
print("0 XOR 0 =", xor_gate(0, 0))
print("0 XOR 1 =", xor_gate(0, 1))
print("1 XOR 0 =", xor_gate(1, 0))
print("1 XOR 1 =", xor_gate(1, 1))
