class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = list(sorted(tokens))
        score = 0

        curl = 0
        curr = len(tokens)-1

        while curl <= curr:
            if power >= tokens[curl]:
                power -= tokens[curl]
                score += 1
                curl += 1
            elif curl+1 < curr and score > 0:
                power += tokens[curr]
                score -= 1
                curr -= 1
            else:
                break
        
        return score
        
        