def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    
    index=0
    count=0
   
    vovels=["a","e", "i"," o", "u"]
   
    while index<len(s):
        if s[index].isalpha() and s[index] not in vovels :
            count+=1
        index+=1
    return count
print(main("a1sfgj ,.rtR 45"))

