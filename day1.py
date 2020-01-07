list1=[]
num=int(input())
for i in range(0,num):
    numbers=int(input())
    list1.append(int(numbers))
for j in range(0,len(list1)):
    list1[j]=0
    for k in range(1,j-1):
        list1[k]=list1[j]+1
        list1[j]=list1[k]
    for m in range(j+1,len(list1)):
        list1[m]=len(list1)
        list1[m]=list1[m]
        list1[-1]=0

list1[-1]=0
print(list1)