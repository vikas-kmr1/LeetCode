class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        var lst = mutableListOf<Int>()
        
        tokens.forEach{
            if(it in listOf("+","*","/","-")){
            
                val a = lst.removeAt(lst.size - 2)
                val b = lst.removeAt(lst.size - 1)
                
                if(it == "+"){
                   lst.add(a+b)
                }
                 
                else if(it == "*"){
                   lst.add(a*b)
                }
                 
                if(it == "/"){
                   lst.add(a/b)
                }
                 
                if(it == "-"){
                   lst.add(a-b)
                }
                
            }
            else{
                lst.add(it.toInt())}
                
        }
        return lst.removeAt(0)
    }
}