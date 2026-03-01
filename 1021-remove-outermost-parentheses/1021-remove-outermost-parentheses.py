




                
class Solution:
    def removeOuterParentheses(self, s):
        stack = []
        res = ''


        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if ch=='(':
                    stack.append(ch)
                    res = res + ch
                else:
                    stack.pop()
                    if not stack:
                        continue
                    res = res + ch
        return res