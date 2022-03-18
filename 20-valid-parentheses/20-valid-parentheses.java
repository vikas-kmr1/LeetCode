class Solution {
    public boolean isValid(String s) {
        
        if (s.length() == 0){
            return false;
        }
        
        Stack <Character> stack = new Stack<>();
        
        for(int i=0; i< s.length(); i++)
        {
            char c = s.charAt(i);
            if ( c == '(' || c == '{' || c == '[')
            {
                stack.push(c);
                continue;
                
            }
            
            if (c == ')'){
                if( !stack.empty() && stack.peek() == '(' ){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            
            if (c == ']'){
                if( !stack.empty() && stack.peek() == '[' ){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            
            if (c == '}'){
                if( !stack.empty() && stack.peek() == '{'){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            
            
            
            
        }
        
        
        if (stack.empty()){
            return true;
        }
        else{
            return false;
        }
        
        
    }
}