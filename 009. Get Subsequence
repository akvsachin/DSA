s = input()

def getSS(s):
    #Write your code here

    if len(s) == 0 :
        empty_ans = [""]
        return empty_ans
    sub_string = s[1:]
    small_ans = getSS(sub_string)
    my_ans = [];
    first_character = s[:1]
    for subs in small_ans:
        my_ans.append(subs)
    
    for subs in small_ans:
        subs = first_character + subs;
        my_ans.append(subs)
    
    return my_ans;
    
ans = getSS(s)

print("["+', '.join(ans) + "]")
