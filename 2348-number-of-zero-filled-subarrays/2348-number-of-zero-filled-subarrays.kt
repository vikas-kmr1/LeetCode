class Solution {
    fun zeroFilledSubarray(nums: IntArray): Long {
        var cnt:Long = 0
        var ans:Long = 0
        
        nums.forEach{
            n ->
            if(n == 0){
                cnt++
            }
            else{
                ans += (cnt * (cnt+1) )/2 
                cnt = 0
            }
        }
        
        if (cnt > 0) {
        ans += (cnt * (cnt+1) )/2 }
        
        return ans
    }
}