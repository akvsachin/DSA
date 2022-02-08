def display(arr,idx,n):
   # Write your code here
    if idx==n:
        return
    print (arr[idx])
    display(arr, idx+1, n)

def main():
  
  # Write your code here
  n=int(input())
  arr=[]
  for i in range(n):
      arr.append(int(input()))
  display(arr,0,n)

main()
