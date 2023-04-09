class Solution {
    fun diagonalPrime(nums: Array<IntArray>): Int {
        var ans = 0
        val n = nums.size
        for (i in 0 until n) {
            if (isPrime(nums[i][i])) {
                ans = maxOf(ans, nums[i][i])
            }
        }
        for (i in n - 1 downTo 0) {
            if (isPrime(nums[n - i - 1][i])) {
                ans = maxOf(ans, nums[n - i - 1][i])
            }
        }
        return ans
    }
    
    private fun isPrime(n: Int): Boolean {
        // Check if the number is less than or equal to 1, return false if it is
        if (n <= 1) {
            return false
        }
        // Loop through all numbers from 2 to
        // the square root of n (rounded down to the nearest integer)
        for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
            // If n is divisible by any of these numbers, return false
            if (n % i == 0) {
                return false
            }
        }
        // If n is not divisible by any of these numbers, return true
        return true
    }
}
