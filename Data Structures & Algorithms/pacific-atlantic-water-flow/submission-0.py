class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find the elements that can flow from Pacific Ocean (up and left)
        Find the elements that can flow from Atlantic Ocean (down and right)
        and find their intersection
        O(n) time
        O(n) space
        """

        def find_next_flow_elements(i: int, j: int) -> list[tuple[int]]:
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]):
                return []
            cur = heights[i][j]
            res = []
            for row, col in (
                (i + 1, j),
                (i, j + 1),
                (i - 1, j),
                (i, j - 1),
            ):
                if 0 <= row < len(heights) and 0 <= col < len(heights[0]):
                    if cur <= heights[row][col]:
                        res.append((row, col))
            return res

        def find_flow_elements(adjacent_elements:list[tuple(int)]) -> set(tuple(int)):
            print("find_flow_elements in")
            print(adjacent_elements)
            ret_elements = set()
            while adjacent_elements:
                (i, j) = adjacent_elements.pop()
                ret_elements.add((i, j))
                for (flow_element_i, flow_element_j) in find_next_flow_elements(i, j):
                    if (flow_element_i, flow_element_j) not in ret_elements:
                        adjacent_elements.append((flow_element_i, flow_element_j))
            print(f"{ret_elements}")
            return ret_elements


        # bfs and find all elements
        flowed = []
        for i in range(len(heights[0])):
            flowed.append((0,i))
        
        for j in range(len(heights)):
            flowed.append((j, 0))

        pacific_elements = find_flow_elements(flowed)

        flowed = []
        for i in range(len(heights[0])):
            flowed.append((len(heights) - 1, i))
        
        for j in range(len(heights)):
            flowed.append((j, len(heights[0]) - 1))

        atlantic_elements = find_flow_elements(flowed)
        
        return list(atlantic_elements & pacific_elements)
        

        

        
                