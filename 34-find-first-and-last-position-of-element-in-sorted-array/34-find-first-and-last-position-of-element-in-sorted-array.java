class Solution {
    public int[] searchRange(int[] nums, int target) {
      int[] ans={-1,-1};
      
       ans[0]=binarySearch(nums,target,true);
       
       ans[1]=binarySearch(nums,target,false);
        
        return ans;
        
        
    }
    
    public int binarySearch(int[] nums,int target,boolean first_searched)
    {
        int ans=-1;
        int start=0;
        int end=nums.length-1;
        
        while(end>=start)
        {
          int mid=(end-start)+start/2;
          if(nums[mid]==target)
          {
              ans= mid;
              if(first_searched)
              {
                  end=mid-1;
              }
              else{
                  start=mid+1;
              }
              
              
          }
          
          else if(nums[mid]>target)
          {
              end=mid-1;
          }
          
            else
            {
                start=mid+1;
            }
            
            
            
            
        }
        return ans;
        
    }
}