class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        return self.go(s, "", 0)
    def go(self, s, sub, idx):
        if idx >= len(s):
            if self.is_valid(sub):
                return [sub]
            return []
        result = []
        dictionary = {}
        if s[idx] == '(' or s[idx] == ')':
            result += self.go(s, sub, idx + 1)
        taken = self.go(s, sub + s[idx], idx + 1)
        result += taken
        maxlen = 0
        if len(result) > 0:
            maxlen = max([len(x) for x in result])
        for r in [x for x in result if len(x) == maxlen]:
            dictionary[r] = True
        return [k for k in dictionary]
    def is_valid(self, s):
        lefts = 0
        for c in s:
            if c == '(':
                lefts += 1
            elif c == ')':
                lefts -= 1
            if lefts < 0:
                return False
        return lefts == 0