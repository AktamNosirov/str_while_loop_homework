def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    def punctuation(s):
        ind=0
        belgilar_list1=[]
        while ind<len(s) :
            if not (s[ind].isdigit() or s[ind].isalpha()):
                belgilar_list1+=[s[ind]]
            ind+=1
        
        return belgilar_list1
        
    index=0
    count=0
    a=punctuation(s)
    vovels=["a","e", "i"," o", "u"]
   
    while index<len(s):
        if not ((s[index] in vovels or s[index].isdigit())) and s[index] not in a:
            count+=1
        index+=1
    return count
print(main("a1sfgj 45"))

