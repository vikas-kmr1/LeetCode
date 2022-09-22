class Solution {
    public static void swap(int[] nums,int i,int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    public static void reverse(int[] nums,int i,int j){
       while( i< j){
           swap(nums,i,j);
           i+=1;
           j--;
       }
    }
    
    
    
    public void nextPermutation(int[] nums) {
        
        if (nums.length <= 1)
        return; 
        
        
        int ind = (nums.length) - 2;
        
        while (ind >= 0 && nums[ind] >= nums[ind+1]) {
            ind--;
        }
        int ind2= nums.length -1;
        if (ind >= 0){
            
            
            while (nums[ind2] <= nums[ind] ){
                ind2--;
            }
            
            swap(nums,ind,ind2);
               
        }
        
        reverse(nums,ind+1,nums.length-1);
         
            
        
            
        
        
        
        
        
    }
}