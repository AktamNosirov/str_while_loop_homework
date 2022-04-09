def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    index=0
    sum=0
   
  
    while index<len(s):
        if s[index].isdigit() :
            sum+=int(s[index])
           
        index+=1
    return sum
print(main("235235"))