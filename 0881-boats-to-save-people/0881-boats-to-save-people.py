class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people = deque(sorted(people))
#         boats = 0
#         while len(people) > 1:
            
#             if people[0] + people[-1] <= limit:
#                 people.popleft()
#                 people.pop()
#             else:
#                 people.pop()
#             boats += 1
        
#         if people:
#             boats += 1
        
#         return boats
            
            
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i