class Solution {
    public int[] sortedSquares(int[] nums) {
        int n=0,p=0;
        while(p<nums.length){
            if(nums[p]>=0){
                break;
            }
            p++;
        }
        int arr[] = new int[nums.length];
        int i=0;
        n=p-1;
        while(p < nums.length && n>=0){
            int f=(int)Math.pow(nums[n],2);
            int s=(int)Math.pow(nums[p],2);
            if(f>s){
                arr[i]=s;
                p++;
            }else{
                arr[i]=f;
                n--;
            }
            i++;
        }
        
        if(n==-1){
            while(p<nums.length){
                arr[i]=nums[p]*nums[p];
                i++;
                p++;
            }
        }else{
            while(n>=0){
                arr[i]=nums[n]*nums[n];
                i++;
                n--;
            }
        }
        return arr;
    }
}