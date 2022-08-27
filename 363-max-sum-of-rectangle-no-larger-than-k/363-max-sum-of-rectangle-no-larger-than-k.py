class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:

        # Get the length of rows and colums
        m, n = len(matrix), len(matrix[0])

        # Initialize the result
        res = -inf

        # Iterate the left pointer from 0 to n
        for l in range(n):

            # Initialize the row prefix sum
            rowSums = [0] * m

            # Iterate the right pointer from left to n
            for r in range(l, n):

                # Calculate the row prefix sum from left to right
                for i in range(m):
                    rowSums[i] += matrix[i][r]

                # Calculate the column prefix sums
                # Initialize a list to store previous column prefix sum
                colSums = [0]

                # Intialize the column prefix sum
                colSum = 0

                # Iterate through all row prefix sums
                for rowSum in rowSums:

                    # Add the current row prefix sum to the column prefix sum
                    colSum += rowSum

                    # Calculate the different between the column prefix sum and k
                    diff = colSum - k

                    # Perform a binary search to find an index of a value is larger but cloest to the target among previously calculated column prefix sums
                    idx = bisect_right(colSums, diff)

                    # Check if the different exists among the previously calculated column prefix sums
                    if idx - 1 >= 0 and colSums[idx - 1] == diff:

                        # If yes, update the result
                        res = max(res, colSum - colSums[idx - 1])

                        # End the search because we found the largest possible result
                        return k

                    # Else, if the different does not exist among the previously calculated column prefix sums, check if there is a previously calculated column prefix sum larger than the target
                    elif idx != len(colSums):

                        # If yes, update the result with the new area if it is larger than previous result
                        res = max(res, colSum - colSums[idx])

                    # Insert the current column prefix sum into the list while maintaining the sorted order
                    insort(colSums, colSum)

        return res