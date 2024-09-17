f=open('okr.txt')

count_shoots=int(f.readline())
count_victory=0

for i in range(count_shoots):
    n,x,y=map(float, f.readline().split())
    if (x**2+y**2)<=n**2:
        count_victory+=1

print(count_victory)
    
    

