class Solution:
    
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def traverse(string,index):
            if len(string) == len(s):
                ans.append(''.join(string[:]))
                return
            else:
                string.append(s[index])
                traverse(string,index+1)
                string.pop(-1)
                if s[index].isalpha():
                    string.append(s[index].swapcase())
                    traverse(string,index+1)
                    string.pop(-1)
                
                
        ans = []
        traverse([],0)
        return ans