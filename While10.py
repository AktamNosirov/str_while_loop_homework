def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    index=0
    sum=0
   
  
    while index<len(s):
        if int(s[index])%2==1 :
            sum+=int(s[index])
           
        index+=1
    return sum
print(main("235235"))