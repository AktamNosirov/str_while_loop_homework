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
    while index<len(s):
        if s[index].isdigit():
            count+=1
            index+=1
        else :        
            index+=1
            
    return count 
print(main("f3"))
   