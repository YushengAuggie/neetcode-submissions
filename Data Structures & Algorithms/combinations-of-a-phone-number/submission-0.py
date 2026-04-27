class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        time: O(n) n is the length of digits 
        space: O(n)
        """
        digit_char_map = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"],
        }

        res = []
        def dfs(index: int, cur_list: List[str]) -> None:
            if index == len(digits):
                if cur_list:
                    res.append("".join(cur_list))
                return
            
            for char in digit_char_map[
                digits[index]
            ]:
                cur_list.append(char)
                dfs(index + 1, cur_list)
                cur_list.pop()
            return

        dfs(0, [])
        return res
