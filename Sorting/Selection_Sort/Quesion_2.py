# Quesion - 2
# find_Duplicate Value in array using selection sort
def findDuplicate(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i-1,n):
            if arr[j]<arr[mini]:
                mini =j
                arr[i],arr[mini]=arr[mini],arr[i]
def minisum(arr):
        findDuplicate(arr)
        duplicate=set()
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                duplicate.add(arr[i])
                return duplicate
      
    
arr=[22,22,55,55]
print("Sorted Array:",minisum(arr))