class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        build the in-degree diagram
        add the no in-degree elements to the str
        and reverse the str

        """ 
        def find_orders(w1:str, w2:str) -> Optional[tuple[str, str]]:
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] != w2[i]:
                    return (w1[i], w2[i])
                i += 1
            if len(w1) > len(w2):
                return ("#", "#")
            return None

        # build 
        in_degrees = defaultdict(set)
        for w in words:
            for c in w:
                in_degrees[c] = set()
        for i in range(1, len(words)):
            orders = find_orders(words[i - 1], words[i])
            if not orders:
                continue
            if orders == ("#", "#"):
                return ""
            w1, w2 = orders
            print(w1, w2)
            in_degrees[w1].add(w2)
        print(in_degrees)
        res = []
        while in_degrees:
            new_free_w = []
            for w in in_degrees:
                if not in_degrees[w]:
                    res.append(w)
                    new_free_w.append(w)
            
            print(f"{new_free_w=}")

            for w in new_free_w:
                del in_degrees[w]
                for k, v in in_degrees.items():
                    if w in v:
                        in_degrees[k].remove(w)
            
            if not new_free_w:
                return ""
                
        
        return "".join(res[::-1])