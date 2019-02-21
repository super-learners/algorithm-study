class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        words2 = []
        for w in words:
            d = {}
            for c in w:
                d[c] = True
            words2.append(d)
        maxval = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                flag = False
                for c in words[i]:
                    if c in words2[j]:
                        flag = True
                        break
                if flag:
                    continue
                if len(words[i]) * len(words[j]) > maxval:
                    maxval = len(words[i]) * len(words[j])
        return maxval