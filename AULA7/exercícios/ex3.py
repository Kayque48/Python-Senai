L1 = [48, 927, 13, 75, 121]
L2 = [99, 84, 51, 21, 105]

L3 = L1 + L2
print(L3)

L3C = L3.copy()
L3C.sort()
L3D = L3C.copy()
L3D.reverse()

print(L3C)
print(L3D)