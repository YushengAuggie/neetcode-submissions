class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str_list = ""
        for s in strs:
            new_s = ""
            for c in s:
                if c == ",":
                    new_s = new_s + "\\,"
                else:
                    new_s += c
            str_list = str_list + new_s + ","
        return str_list

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []

        ret_list = []
        cur_s = ""
        prev_slash = False
        for c in s:
            if c == ",":
                if prev_slash:
                    cur_s = cur_s[:-1] + ","
                else:
                    ret_list.append(cur_s)
                    cur_s = ""
                prev_slash = False
            else:
                cur_c = c
                if c == "\\":
                    prev_slash = True
                else:
                    prev_slash = False
                cur_s = cur_s + cur_c
        
        # ret_list.append(cur_s)
        return ret_list
