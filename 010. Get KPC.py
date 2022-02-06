s = input()
keypad = (".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz")

def getKPC(s):
    #Write your code here
    if len(s) == 0:
        empty_ans = [""]
        return empty_ans
    new_question = s[1:]
    small_ans = getKPC(new_question)
    ans = []
    first_character = s[:1]
    idx = int(first_character)
    for letter in keypad[idx] :
        for element in small_ans :
            element = letter + element
            ans.append(element)
    return ans
    
ans = getKPC(s)
print("["+', '.join(ans) + "]")
