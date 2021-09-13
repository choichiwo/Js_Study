## 소수 만들기
for a in range(2,1001):
    c=0    
    for b in range(2,a):
        if a%b==0:
            c=1
    if c==0:
        print(a,end=',')