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
    consonant=["a","e", "i"," o", "u"]
    while index<len(s):
        if not (s[index] in consonant or s[index].isdigit())  :
            count+=1
        index+=1
    return count 
print(main("a1s"))