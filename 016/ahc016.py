M, eps = input().split()
M = int(M)
eps = float(eps)
N=0
for i in range(4,101):
    if i**2-i>=M*2:
        N=i
        break
print(N)
for k in range(M):
    print("1" * k + "0" * ((N**2-N)//2 - k))

for q in range(100):
    H = input()
    t = min(H.count('1'), M - 1)
    print(t)

