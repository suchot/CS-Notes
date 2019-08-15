class Solution:
    def numSquares(self, n: int) -> int:
        if n<4:
            return n
        visited = [0 for i in range(n+1)]
        queue = [0]
        while queue:
            ele = queue.pop(0)
            for i in range(1, n+1):
                if ele + i**2 > n:
                    break
                elif ele + i**2==n:
                    return visited[ele]+1
                elif visited[ele + i**2] == 0:
                    queue.append(ele + i**2)
                    visited[ele + i**2] = visited[ele] +1
        return visited[n]

if __name__ == "__main__":
    S =Solution()
    print(S.numSquares(13))
