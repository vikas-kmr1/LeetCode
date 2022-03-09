class Solution {
    public int romanToInt(String s) {
        
char [] a =  s.toCharArray();
int  prev = 0;
int RunningSum =0;
        
  Map<Character, Integer> lookup = new HashMap<Character, Integer>();
lookup.put('I', 1);
lookup.put('V', 5);
lookup.put('X', 10);
lookup.put('L', 50);
lookup.put('C', 100);
lookup.put('D', 500);
lookup.put('M', 1000);

        
        for (char letter : a){
            int letterAsNum = lookup.get(letter);
            
            if (prev < letterAsNum){      int number = (prev - letterAsNum)*(-1);RunningSum = RunningSum + number - prev;   }
            else { RunningSum = RunningSum + letterAsNum;}
            prev = letterAsNum; //update previous
            
        }
        
     return RunningSum;   
    }
}