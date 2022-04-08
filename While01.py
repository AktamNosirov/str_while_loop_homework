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
        count+=1
        index+=1
    return count
print(main("12345"))
   