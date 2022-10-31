class Solution {
    fun isPalindrome(x: Int): Boolean {
        var res= 0
        var x_c = x
        while (x_c > 0){
            res = (res * 10) + (x_c % 10)
            x_c /= 10
        }
        
        return (res == x)
        
    }
}