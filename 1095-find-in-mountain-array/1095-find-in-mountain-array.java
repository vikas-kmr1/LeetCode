/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        
        return findMax(target,mountainArr);
        
    }
    
    
    public int findMax(int target,MountainArray arr ) 
    {
        int start=0;
        int end= arr.length() - 1 ;
        while(start<end)
        {
            int mid=start + (end-start)/2 ;
            if (arr.get(mid)> arr.get(mid+1))
            {
                end=mid;
            }
            else
            {
                start=mid+1;
            }
        
        }
        
        int f=binaryAS(target,arr,0,end); 
        if (f == -1)
        {
             return binaryDS(target,arr,end,arr.length() -1)   ;     
        }
                
        return f;
        
    }
                
     public int binaryAS(int target,MountainArray arr,int start,int end) 
    {
        if(start<=end)
        {
            int mid=start+(end-start)/2;
            
            if(arr.get(mid)==target)
            {
                return mid;
                
            }
            
            else if(arr.get(mid)>target){
                
                return binaryAS( target,arr,start,mid-1);              
            }
            
              else {
                
                return binaryAS( target,arr,mid+1,end);             
            }
            
            
        }
        
        
       return -1; 
    }        
    
    
    
     public int binaryDS(int target,MountainArray arr,int start,int end) 
    {
        if(start<=end)
        {
            int mid=start+(end-start)/2;
            
            if(arr.get(mid)==target)
            {
                return mid;
                
            }
            
            else if(arr.get(mid)<target){
                
                return binaryDS( target,arr,start,mid-1);              
            }
            
              else {
                
                return binaryDS( target,arr,mid+1,end);             
            }
            
            
        }
        
        
       return -1; 
    }            
    
    
}



