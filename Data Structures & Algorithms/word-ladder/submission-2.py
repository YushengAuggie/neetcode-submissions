class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ByteString,
        The logic here is that we basically have a queue.
        Every time we transform one word,
         we find the word it can transform to and mark that word as visited.
         Then the next step is just to transform it to a different word until
          we find the target. The first path that reaches the target is the nearest,
           or shortest path.

        the tricky part is how we save the path. Actually,
         we just need to save the steps, so that's easy.
          We just need to save the steps, and then that's fine.
          If there's no solution, we just return zero.


        In the worst case, we need to go through every single word.

        So the time complexity will be O(n) -> O(n^2 * m) m = length of each word
         Since we save everything into the queue,
          the space complexity will also be O(n).
        """

        queue = []
        queue.append(beginWord)
        visited = set(beginWord)
        step = 1

        def can_transform(w1: str, w2: str) -> bool:
            """
            Whether w1 can be transformed to w2 with one character replacement.
            """
            if len(w1) != len(w2):
                return False
            count_diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    count_diff += 1
                    if count_diff == 2:
                        return False
            return True

        while queue:
            next_queue = []

            while queue:
                cur_word = queue.pop()
                if cur_word == endWord:
                    return step

                for word in wordList:
                    if word not in visited and can_transform(cur_word, word):
                        visited.add(word)
                        next_queue.append(word)
            step += 1
            queue = next_queue
        return 0
