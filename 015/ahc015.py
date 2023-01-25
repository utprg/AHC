def  move(grid,d):
     while True:
         move_count=0
         if d=="F":
           for i in range(len(grid)-1):
              for j in range(len(grid)):
                   if  grid[i][j]==0 and grid[i+1][j]!=0:
                       grid[i][j]=grid[i+1][j]
                       grid[i+1][j]=0
                       move_count+=1
         if d=="B":
           for i in range(len(grid)-1):
              for j in range(len(grid)):
                   if  grid[i+1][j]==0 and grid[i][j]!=0:
                       grid[i+1][j]=grid[i][j]
                       grid[i][j]=0
                       move_count+=1
         if d=="L":
           for i in range(len(grid)):
              for j in range(len(grid)-1):
                   if  grid[i][j]==0 and grid[i][j+1]!=0:
                       grid[i][j]=grid[i][j+1]
                       grid[i][j+1]=0
                       move_count+=1
         if d=="R":
           for i in range(len(grid)):
              for j in range(len(grid)-1):
                   if  grid[i][j+1]==0 and grid[i][j]!=0:
                       grid[i][j+1]=grid[i][j]
                       grid[i][j]=0
                       move_count+=1
         if move_count==0:
              break
     
                   
import random
f=list(map(int,input().split()))
d=["F","B","L","R"]
grid=[[0 for _  in range(10)] for _ in range(10)] 
for i in range(100):
    p=int(input())
    while p!=0:
           
    t=random.randrange(4)
    print(d[t],flush=True)
