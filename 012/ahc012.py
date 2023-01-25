n,k=map(int,input().split())
a=list(map(int,input().split()))
berryx=[]
berryy=[]
for i in range(n):
 x,y=list(map(int,input().split()))
 berryx.append(x)
 berryy.append(y)
cut_list=[]
for j in range(max(berryx)):
 if j not in berryx:
  cut_list.append(j)
  for m in [j+1,max(berryx)+1]:
   counter=0
   if m in berryx:
    counter+=1
    if counter==10:
     cut_list.append(m+1)




print(k)
for i in range(k):
 print(cut_list[2*i],0,cut_list[2*i+1],1000)
