n = int(input())
m = int(input())

def get_maze_paths(sr, sc, dr, dc):
    #Write your code here
    if sc == dc and sr == dr:
        empty_ans = [""]
        return empty_ans

    ans = []

    for jump in range(1, dc+1):
        if sc+jump <= dc:
            horizontal_path = get_maze_paths(sr, sc+jump, dr, dc)
            for path in horizontal_path:
                path =  "h" + str(jump) + path
                ans.append(path)
    
    for jump in range(1, dr+1):
        if sr+jump <= dr:
            vertical_path = get_maze_paths(sr+jump, sc, dr,dc)
            for path in vertical_path:
                path = "v" + str(jump) + path
                ans.append(path)

    for jump in range (1, max(dr, dc)+1):
        if sr+jump <= dr and sc+jump <= dc:
            diagonal_path = get_maze_paths(sr+jump, sc+jump, dr, dc)
            for path in diagonal_path:
                path = "d" + str(jump) + path
                ans.append(path)       

    return ans 
    
    
ans = get_maze_paths(0, 0, n-1, m-1)

print("["+', '.join(ans) + "]")
