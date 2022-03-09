class Solution {
    public boolean isPalindrome(int x) {
        
        System.out.println(checkP(x,0));
         if(checkP(x,0)!=x || x<0)
         {
             return false;
        }
        return true;
    
    }
    
    public int checkP(int x,int temp)
    {
    // base case
    if (x == 0)
        return temp;
 
    // stores the reverse of a number
    temp = (temp * 10) + (x % 10);
 
    return checkP(x / 10, temp);
    }
    
}