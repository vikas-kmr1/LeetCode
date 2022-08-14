class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

		for i in range(len(mat)):
			res = str(mat[i]).count("1")
			mat[i] = [i,res]

		mat.sort(key=lambda x : x[1])
		n = len(mat)

		for i in range(n):
			temp = mat[i][0]
			mat[i] = temp
		return mat[:k]