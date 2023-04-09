class Solution {
    public int diagonalPrime(int[][] nums) {
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (isPrime(nums[i][i])) {
                ans = Math.max(ans, nums[i][i]);
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (isPrime(nums[n - i - 1][i])) {
                ans = Math.max(ans, nums[n - i - 1][i]);
            }
        }
        return ans;
    }
    
    private boolean isPrime(int n) {
        // Check if the number is less than or equal to 1, return false if it is
        if (n <= 1) {
            return false;
        }
        // Loop through all numbers from 2 to
        // the square root of n (rounded down to the nearest integer)
        for (int i = 2; i <= Math.sqrt(n); i++) {
            // If n is divisible by any of these numbers, return false
            if (n % i == 0) {
                return false;
            }
        }
        // If n is not divisible by any of these numbers, return true
        return true;
    }
}
