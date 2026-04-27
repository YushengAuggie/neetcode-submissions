from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Build a graph
        for every course, we have a dependency
        course_unblock = {course_a: courses that depend on a}
        course_dependency = {course_num: n} n is the dependency count

        we firstly pop out and take all course_num = 0
        and the next steps for every course we already take we go over the 
        course_unblock and cut course_dependency value for unblocked courses

        so for every course we will need to 


        time: O(n + m) numCourses + len(prerequisites)
        space: O(m + n) numCourses + len(prerequisites)

        """

        course_unblock = defaultdict(list[int])
        course_dependency = defaultdict(int)
        course_queue = []

        taking_order = []

        for course, pre_course in prerequisites:
            course_unblock[pre_course].append(course)
            course_dependency[course] += 1
        
        for course in range(numCourses):
            if course not in course_dependency:
                course_queue.append(course)

        # print("course_unblock", course_unblock)
        # print("course_dependency", course_dependency)
        # print("course_queue", course_queue)


        while course_queue:
            cur = course_queue.pop()
            for course in course_unblock[cur]:
                course_dependency[course] -= 1
                if course_dependency[course] == 0:
                    course_queue.append(course)
            
            taking_order.append(cur)

        # print(taking_order, len(taking_order))
        return taking_order if len(taking_order) == numCourses else []


            