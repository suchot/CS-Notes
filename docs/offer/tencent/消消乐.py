from collections import Counter
class Solution():
    def xiaoxiao(self, numbers):
        # write code here
        thred = len(numbers)/2
        dict_num = Counter(numbers)
        for key,value in dict_num.items():
            if value> thred:
                return 'NO'
        return 'YES'
if __name__ == "__main__":
    T = int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    S = Solution()
    for i in range(T):
        print(S.xiaoxiao(arr))