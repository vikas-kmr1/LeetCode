class Solution:
    def maximumValue(self, strs: List[str]) -> int:
    
    # initialize the maximum value to 0
        max_value = 0

    # iterate through the strings in the array
        for s in strs:
        # check if the string is numeric
            if s.isnumeric():
            # convert the string to base 10 and compare it to the current maximum value
                max_value = max(max_value, int(s))
            else:
            # compare the length of the string to the current maximum value
                max_value = max(max_value, len(s))

        return max_value
     