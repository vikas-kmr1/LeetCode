class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:

        # Expand buildings to account for the start and end of each building. We know a tuple is an end of a building if its height is 0
        buildings = sorted(
            [(start, -height, end) for start, end, height in buildings]
            + [(end, 0, None) for _, end, _ in buildings]
        )

        # Initialize heap and result
        heap, res = [(0, inf)], [(0, 0)]

        # Iterate through all buildings
        for start, height, end in buildings:

            # If there is a builing that end before the current start, remove it from the heap
            while start >= heap[0][1]:
                heapq.heappop(heap)

            # If the current height is greater than 0, add it along with the current end onto the heap
            if height:
                heapq.heappush(heap, (height, end))

            # Find the max height
            maxHeight = -heap[0][0]

            # If the current max height is different from the previous max height, add the current start and max height onto the result
            if maxHeight != res[-1][1]:
                res.append([start, maxHeight])

        return res[1:]