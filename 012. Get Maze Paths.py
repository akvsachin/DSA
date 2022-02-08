n = int(input())
m = int(input())

def get_maze_path(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        empty_ans = [""]
        return empty_ans
    my_ans = []
    if sc+1 <= dc:
        horizontal_small_ans = get_maze_path(sr, sc+1, dr, dc)
        for element in horizontal_small_ans:
            element = "h" + element
            my_ans.append(element)
    if sr+1 <= dr:
        vertical_small_ans = get_maze_path(sr+1, sc, dr, dc)
        for element in vertical_small_ans:
            element = "v" + element;
            my_ans.append(element)
    return my_ans

ans = get_maze_path(0,0,n-1,m-1)
print("["+', '.join(ans) + "]")
