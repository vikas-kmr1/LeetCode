class Solution {
    public int removeDuplicates(int[] nums) {
          int k = 0;
        int same = nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=same){
                same=nums[i];
                nums[i-k]=nums[i];
            }
            else{
                k++;
            }
        }
        return nums.length-k;
    
        
    }
}