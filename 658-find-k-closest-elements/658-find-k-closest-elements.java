class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int n=arr.length,diff[]=new int[n],i; 
        List<Integer> list = new ArrayList<Integer>();
        int min=Integer.MAX_VALUE,index=-1;
        
        for(i=0;i<n;i++){ 
            diff[i]=Math.abs(arr[i]-x);
            if(min>diff[i]){
                min=diff[i];
                index=i;
            }
        }
        
        int left=index,right=index+1;
        for(i=0;i<k;i++){
            if(left>=0 && ((right<n && diff[left]<=diff[right]) || right==n)){
                list.add(arr[left]);
                left--;
            }else { 
                list.add(arr[right]);
                right++;
            }
        }
        Collections.sort(list);
        return list;
    }

}