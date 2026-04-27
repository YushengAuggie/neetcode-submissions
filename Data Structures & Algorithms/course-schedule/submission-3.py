from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        O(n + e) n is number of courses and e is the prerequisites edges
        O(n)
        """

        pre_course_map = defaultdict(list[int])
        
        for course, pre in prerequisites:
            pre_course_map[course].append(pre)

        for num in range(numCourses):
            if num not in pre_course_map:
                pre_course_map[num] = []

        visited = set() 
        def dfs(course: int) -> bool:
            """ if can take this course without cycle."""

            if course in visited:
                return False

            if len(pre_course_map[course]) == 0:
                return True
            
            visited.add(course)
            for pre in pre_course_map[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            pre_course_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True