if __name__ == "__main__":

    def solution(s, k):
        if len(s) < k:
            return "false"
        
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = 1
            else:
                lookup[s[i]] += 1
        
        number = 0
        for val in lookup.values():
            if val&1:
                number += 1
                
        if number > k:
            return "false"
        
        return "true"

    def fastsolution(s, k):
        import collections
        return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)

    print(solution("annabelle", 2))
    print(fastsolution("annabelle", 2))

    print(solution("leetcode", 3))
    print(fastsolution("leetcode", 3))