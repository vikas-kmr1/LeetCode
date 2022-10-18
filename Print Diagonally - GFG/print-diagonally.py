#User function Template for python3

def downwardDigonal(N, A): 
    
    diagonal_map = {}
    
    for row in range(N):
        for column in range(N):
            if (row + column) in diagonal_map:
                diagonal_map[row + column].append(A[row][column]) 
            
            else:
                diagonal_map[row + column] = [A[row][column]]
    
    ans = []
    for mat in diagonal_map.values():
        ans.extend(mat)
    
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends