def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    index=0
    count=0
   
  
    while index<len(s):
        if int(s[index])%2==1 :
            count+=1
           
        index+=1
    return count
print(main("235235"))