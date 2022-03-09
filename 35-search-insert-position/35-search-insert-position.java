class Solution {
    public int searchInsert(int[] nums, int target) {
        
    return binarySearch(nums,target,0,nums.length -1 );
    }
    
    public int binarySearch(int[] nums,int target,int start,int end)
    {
        if (start<=end)
        {
            if (nums[start+(end-start)/2]==target)
            {
                return start+(end-start)/2;
            }
            else if (nums[start+(end-start)/2]<target)
            {
                return binarySearch(nums,target,(start+(end-start)/2)+1,end);
            }
            else{
                return binarySearch(nums,target,0,(start+(end-start)/2)-1);
            }
            
        }
        else {return start;}
        
    }
}
