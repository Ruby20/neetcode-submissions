class Solution:
    def isValid(self, s: str) -> bool:
        # stack and a reference map
        valid_mapping = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        parens = []

        for char in s:
            if char in ["(", "{", "["]:
                parens.append(char)
            else:
                if parens:
                    if parens[-1] != valid_mapping[char]:
                        return False
                    else:
                        parens.pop()    
                else:
                    return False    

        return len(parens) == 0                    