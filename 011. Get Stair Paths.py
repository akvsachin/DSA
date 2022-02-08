n = int(input())

def get_stair_paths(n):
    #Write your code here
    if n==0:
        empty_ans = [""]
        return empty_ans
        
    ans = []
    
    for step in range(1,4):
        if (n-step) >=0:
            small_ans = get_stair_paths(n-step)
            for element in small_ans:
                element = str(step) + element;
                ans.append(element)
    
    return ans
    
ans = get_stair_paths(n)

print("["+', '.join(ans) + "]")
