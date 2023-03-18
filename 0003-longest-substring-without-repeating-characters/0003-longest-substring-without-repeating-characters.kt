class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var sets= mutableSetOf<Char>()
        
        var l = 0
        var ans = 0
        for(i in 0.. s.length-1 ){
            while(sets.contains( s[i] ) ){
                sets.remove(s[l])
                 l += 1
            }
            sets.add(s[i])
            ans = maxOf(ans,i-l+1)
            
        }
        return ans
        
    }
}