class TrieNode(){
val children = mutableMapOf<Char,TrieNode>() 
var endOfWord:Boolean = false    
}

class Trie(
val root:TrieNode = TrieNode() 
) {

    fun insert(word: String) {
        var curr  = this.root
        
        for(c in word){
            if(!(c in curr.children)){
                curr.children.put(c,TrieNode())
            }
            curr = curr.children[c]!!
        }
        curr.endOfWord = true
    }

    fun search(word: String): Boolean {
        var curr = this.root
        
        for(c in word){
            if (!(c in curr.children)){
                return false
            }
            curr = curr.children[c]!!
        }
        return curr.endOfWord
        
    }

    fun startsWith(prefix: String): Boolean {
        var curr = this.root
        
        for(c in prefix){
            if (!(c in curr.children)){
                return false
            }
            curr = curr.children[c]!!
        }
        return true
        
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */