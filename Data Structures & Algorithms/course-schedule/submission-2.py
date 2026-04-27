from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        dfs 
        remove nodes does not have dependencies, and keep doing this

        how to handle cycle?
        how to find nodes that are free (do not have dependencies)?
        
        # iterate the whole set again and again and if no new node is coming out, then there's a cycle
        E + V 



        """
        dependencies = defaultdict(list[int])
        free_courses = set()
        for course, prec in prerequisites:
            dependencies[course].append(prec)
        print(dependencies)

        for i in range(numCourses):
            if i not in dependencies:
                free_courses.add(i)
        while len(free_courses) < numCourses:
            new_dependencies = defaultdict(list[int])
            for course, precs in dependencies.items():
                if all(prec in free_courses for prec in precs):
                    free_courses.add(course)
                    print(f"free {precs} add {course}")
                else:
                    new_dependencies[course]=precs
                    print(f"still need {course}:{precs} ")
            if len(new_dependencies) == len(dependencies):
                # cycle
                return False
            dependencies = new_dependencies

        return True
