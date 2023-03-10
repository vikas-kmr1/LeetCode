class Solution {
    fun maxArea(height: IntArray): Int {
        var start = 0
        var end = height.size - 1
        
        var maxAmt = 0
        while (start < end) {
            val minHeight = minOf(height[start], height[end])
            val xDistance = end - start
            
            maxAmt = maxOf(maxAmt, minHeight * xDistance)
            
            when (height[start] < height[end]) {
             true ->  start++
             else -> end-- }
        }
        
        return maxAmt
    }
}