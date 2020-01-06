def pop(arr1):
    arr=[]
    for i in range(len(arr1)):
        arr.append(arr1[i])
    for i in range(0,len(arr1)):
        if(arr1[i]>1):
            water=arr1[i]
            for j in range(i-1,-1,-1):
                arr[j]+=water-1
                water-=1
                if(water==0):
                    break
            water=arr1[i]
            for k in range(i+1,len(arr)):
                arr[k]+=water-1
                water-=1
                if(water==0):
                    break
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(pop(arr))
