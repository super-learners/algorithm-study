class Solution:
    def largestTimeFromDigits(self, A: 'List[int]') -> 'str':
        latest = {
            "hour": None,
            "min": None
        }
        for p in self.next_permutation(A):
            if p[0] > 2:
                continue
            if p[0] == 2 and p[1] > 3:
                continue
            if p[2] > 5:
                continue
            time = {
                "hour": p[0] * 10 + p[1],
                "min": p[2] * 10 + p[3]
            }

            if self.is_later(time, latest):
                latest = time
        if latest["hour"] is None:
            return ""
        return self.to_padded_str(latest["hour"]) + ":" + self.to_padded_str(latest["min"])

    def to_padded_str(self, num):
        if num < 10:
            return "0" + str(num)
        return str(num)

    def is_later(self, time1, time2):
        if time2["hour"] is None:
            return True
        elif time1["hour"] > time2["hour"]:
            return True
        elif time1["hour"] < time2["hour"]:
            return False

        if time1["min"] > time2["min"]:
            return True
        return False

    def next_permutation(self, A: 'List[int]') -> 'List[int]':
        for i, e in enumerate(A):
            if len(A) == 1:
                yield [e]
            else:
                for sp in self.next_permutation(A[0:i] + A[i + 1:]):
                    yield [e] + sp