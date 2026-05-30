from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        So the first version of it could be that we create the interval for every letter, representing the first and last occurrence. Then we merge the overlapping intervals and find the length of the intervals, which is actually the longest substring there.
        In this case, the time complexity would be O(n) because we basically go through every letter once and merge the internals. So, I think it will be O(n) and the space will be O(1), excluding the output.
        """

        # construct internals
        occurrence = defaultdict(list[int])

        for idx, num in enumerate(s):
            if num not in occurrence:
                occurrence[num] = [idx, idx]
            else:
                occurrence[num] = [occurrence[num][0], idx]
        
        # print(occurrence)
        
        # we have interval range()s in time based / chronological order
        merged_intervals = []
        for start, end in occurrence.values():
            if merged_intervals and (
                merged_intervals[-1][1] > start 
            ):
                # print("merge: ", merged_intervals[-1], " and ", start, end, )
                merged_intervals[-1] = [
                    min(start, merged_intervals[-1][0]),
                    max(end, merged_intervals[-1][1])
                ]
            else:
                merged_intervals.append([start, end])
            # print("add ", merged_intervals[-1], "\n\n")

        # print(merged_intervals)
        return [end - start + 1 for start, end in merged_intervals]
                    
