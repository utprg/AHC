w=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[-1,0],[1,-1]]
k=0
N,M=map(int,input().split())
marked=[]
for i in range(M):
 dot=list(map(int,input().split()))
 marked.append(dot)
marked.sort()