## 소수 만들기
for a in range(2,100):
    c=0    
    for b in range(2,a):
        if a%b==0:
            c=1
    if c==0:
        print(a)

#구구단
for i in range(2,10):
    for j in range(1,10):
        print("{}X{}={}".format(i,j,i*j))        