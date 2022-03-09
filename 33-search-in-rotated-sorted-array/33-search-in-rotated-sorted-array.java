class Solution {
     public int search(int[] nums, int target) {
        
      int pivot= SearchPivot(nums,0,nums.length -1);
      System.out.println(pivot);
            
       int ind= binaryAs(nums,0,pivot,target);
         System.out.println(ind);
    
         if(ind==-1)
         {
             return binaryAs(nums,pivot+1,nums.length-1,target);
         }
         
         return ind;
    
    }
    
     public int SearchPivot(int[] arr,int start,int end) 
    {
       while(start<end)
       {
           int mid=start+(end-start)/2;
           if(mid>start && arr[mid]<arr[mid-1])
           {
               return mid-1;
              
           }
            
           else if(mid<end &&arr[mid]>arr[mid+1])
           {
               return mid;
           }
           
           else if(arr[start]>=arr[mid])
              
           {
              end=mid-1; 
           }
           
           else
           {
               start=mid+1;
           }
           
           
              
           
           
       }
             
       return -1;  
    }            
    
    
    
     public int binaryAs(int[] arr,int start,int end,int target) 
    {
        if(start<=end)
        {
            int mid=start+(end-start)/2;
            
            if(arr[mid]==target)
            {
                return mid;
                
            }
            
            else if(arr[mid]>target){
                
                return binaryAs( arr,start,mid-1,target);              
            }
            
              else {
                
                return binaryAs( arr,mid+1,end,target);             
            }
            
            
        }
        
        
       return -1; 
    }            
}