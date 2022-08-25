class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length -1 ;
        int amt = 0;
        while(start < end){
            
            int min_hgt = Math.min(height[start] , height[end]);
            
            amt = Math.max(amt, min_hgt * (end -start));
            
            if(height[start] < height[end]){
                start++;
            }
            
            else{
                end--;
            }
            
            
        }
        
        return amt;
        
    }
}