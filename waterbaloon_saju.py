arr=[0,0,0,0,0,5,0,0,0,0,0,0]
mid=0
flag=0
for i in range(0,len(arr)):
    if arr[i]>1:
        flag=1
        mid=arr[i]
        for j in range(i-1,-1,-1):
            arr[j]+=mid-1
            mid=mid-1
            if mid==0:
                break
        mid=arr[i]
        for k in range(i+1,len(arr)):
            arr[k] += mid-1
            mid = mid - 1
            if mid == 0:
                break
    if(flag==1):
        break
print(arr)