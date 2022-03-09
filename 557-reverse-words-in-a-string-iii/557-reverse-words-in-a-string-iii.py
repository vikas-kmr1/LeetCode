class Solution:
    def reverseWords(self, s: str) -> str:
        st=[]
        st.extend(map(str,s.split(" ")))
        s_new=""
        for i in st:
            s_new +=i[-1: :-1]+" "
        return s_new.rstrip()
        
            
            