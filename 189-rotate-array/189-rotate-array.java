class Solution {
public void rotate(int[] nums, int k) {
int n = nums.length;
k = k % n;
reverse(nums, 0, n - k - 1);
reverse(nums, n - k, n - 1);
reverse(nums, 0, n - 1);
}
public static void reverse(int[] nums, int i, int j){
int li = i;
int ri = j;
while(li < ri){
int temp = nums[li];
nums[li] = nums[ri];
nums[ri] = temp;
li++;
ri--;
}
}
}