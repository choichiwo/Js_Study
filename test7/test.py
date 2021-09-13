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

#글짜 입력
print("Hello",end=" & ")
print("World")       

#함수 활용
def makeBlank(n):
    return n*' '

for i in range(1,11):
    print(makeBlank(i)+'*')


#리스트 활용
l1=[1,100,25,47,-12,5,-1234]
for i in l1:
    print(i)


for i in range(len(l1)):
    print(l1[i])  

l=[]
l.append(12)
l.append("My name")
l.append([10,9,8])
l.remove(12)
for i in l:
    print(i)    

# Tuple(튜플): 리스트와 동일하나, 수정불가!!!!
x=10
y=20
x,y=y,x
print(x,y)   

#Set(집합): 리스트와 동일, 수정가능, 중복값 불허
l1=[10,20,30,10,20,30]          #len(l1) ==6
t1=(10,20,30,10,20,30)          #len(t1) ==6
s1={10,20,30,10,20,30}          #len(s1) ==3 중복제외해서

# s1={}
# while True:
#     n=input("new Value =")
#     s1.append(n)

# Dictionary(사전) : key,value couple(쌍), 중복 값 허용 index없음
d1={'name':'Choi chi','age':23}    
d1['owner']='John'
d1['name']='John'
print(d1)

for i in d1: #print only keys
    print(i)

for i in d1.values(): #print only values
    print(i)

for i,j in d1.items(): #print only key/value by using Tuple
    print(i,j)