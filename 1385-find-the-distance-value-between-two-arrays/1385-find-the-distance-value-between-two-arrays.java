public class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        
        int ans = 0;
        for (int i = 0; i < arr1.length; i++) {
            int low = 0, high = arr2.length - 1;
            boolean isValid = true;
            while (low <= high) {
                int middleIndex = low + (high - low) / 2;
                if (Math.abs(arr1[i] - arr2[middleIndex]) <= d) { 
                    isValid = false;
                    break; 
                }
                if (arr2[middleIndex] < arr1[i]) low = middleIndex + 1;
                else high = middleIndex - 1;
            }
            
            if (isValid)
                ans++;
        }
        
        return ans;
    }
}