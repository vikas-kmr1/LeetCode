class Solution {
    public int[] sortedSquares(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int[] result = new int[nums.length];
        int i = result.length - 1; 
            
        while (i >= 0) {
            int left = Math.abs(nums[l]);
            int right = Math.abs(nums[r]);
            
            if (left >= right) {
               result[i] = left * left;
                l++;
            } else {
                result[i] = right * right;
                r--;
            }
            
            i--;
        }  
        
        return result; 
    }
}

