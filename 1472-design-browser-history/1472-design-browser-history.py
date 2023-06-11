class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.current = 0   
        
    def visit(self, url: str) -> None:
        self.browser = self.browser[:self.current+1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        steps = max(0,self.current - steps)
        
        self.current = steps 

        return self.browser[steps]

   
    def forward(self, steps: int) -> str:
        steps = min( len(self.browser) - 1 , self.current + steps)
        self.current = steps
        return self.browser[steps]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)