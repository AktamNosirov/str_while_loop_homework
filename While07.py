def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    index=0
    count=0
   
  
    while index<len(s):
        if s[index].isdigit() :
            count+=1
           
        index+=1
    return count
print(main("Codes56ch8oolUz55"))