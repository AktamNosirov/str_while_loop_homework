def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    index=0
    count=0
    while index<len(s):
        if s[index].isalpha():
            count+=1
        index+=1
    return count 
print(main("a7yjh65tyhh4"))