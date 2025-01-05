# A
A = [[0, 0, 0] for _ in range(3)]
A[0][0], A[0][1], A[0][2] = 1, 1, 1
A[1][0] = 1

# B
B = [[0, 0, 0] for _ in range(3)]
B[0][1], B[1][1], B[2][1] = 1, 1, 1

# C
C = [[0, 0, 0] for _ in range(3)]
C[1][0], C[1][1], C[1][2] = 1, 1, 1

# D
D = [[0, 0, 0] for _ in range(3)]
D[0][0], D[0][2], D[2][0], D[2][2] = 1, 1, 1, 1

# E
E = [[0, 0, 0] for _ in range(3)]
E[0][1], E[1][0], E[1][1], E[1][2], E[2][1] = 1, 1, 1, 1, 1

print("A:")
for row in A:
    print(row)

print("B:")
for row in B:
    print(row)

print("C:")
for row in C:
    print(row)

print("D:")
for row in D:
    print(row)

print("E:")
for row in E:
    print(row)
