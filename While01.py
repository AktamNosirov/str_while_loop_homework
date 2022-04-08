def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
        
    """
    index=0
    count=0
    while s[index].isdigit() :
        index+=1
        count+=1
        if index==len(s):
            break 
        
    return count
print(main("12345"))
   