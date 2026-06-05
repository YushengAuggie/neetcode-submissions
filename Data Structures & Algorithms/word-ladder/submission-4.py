class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        So the time complexity will be O(n) -> O(n^2 * m) m = length of each word
         Since we save everything into the queue,
          the space complexity will also be O(n).
        """

        queue = []
        queue.append(beginWord)
        visited = set(beginWord)
        step = 1

        wild_card_dict = collections.defaultdict(list[str])

        def _get_wild_card_key(w1: str, idx:int) -> str:
            return w1[:idx] + "*" + w1[idx + 1:]

        for word in wordList:
            for idx in range(len(word)):
                wild_card_key = _get_wild_card_key(word, idx)
                wild_card_dict[wild_card_key].append(word)
        
        # print(wild_card_dict)

        while queue:
            next_queue = []

            while queue:
                cur_word = queue.pop()
                if cur_word == endWord:
                    return step

                for idx in range(len(cur_word)):
                    wild_card_key = _get_wild_card_key(cur_word, idx)
                    for word in wild_card_dict[wild_card_key]:
                        if word not in visited:
                            visited.add(word)
                            next_queue.append(word)
            step += 1
            queue = next_queue
        return 0
