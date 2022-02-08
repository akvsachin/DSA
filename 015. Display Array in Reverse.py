def displayinrev(arr,idx,n):
   
   # Write your code here
    if idx==n:
       return
    displayinrev(arr,idx+1,n)
    print (arr[idx])
    

def main():
    n=int(input())
    arr=[]
    for i in range(n):
      arr.append(int(input()))
    displayinrev(arr,0,n)
main()    
