import sys
sys.setrecursionlimit (10000)
def Firstindex(arr,idx,x,n):
    # Write your code here
    if idx==n:
        return -1;
    if arr[idx]==x:
        return idx;
    else:
        ans=Firstindex(arr,idx+1,x,n)
        return ans

def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    x=int(input())
    ans=Firstindex(arr,0,x,n)
    print(ans)
main()    
