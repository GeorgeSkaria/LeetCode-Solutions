class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = sum(1 for i in range(k) if blocks[i]=='W')
        res = white
        b = k

        while b < len(blocks):
            if blocks[b-k] == 'W':
                white -= 1
            if blocks[b] == 'W':
                white += 1
            res = min(res,white)
            b += 1

        return res




        
