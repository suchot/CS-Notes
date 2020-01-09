class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for i in range(0, len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                self.swap(numbers, i, numbers[i])
        return False
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
if __name__ == "__main__":
    S = Solution()
    numbers = [2, 3, 1, 0, 2, 5]
    d = [0]
    print(S.duplicate(numbers,d))
    print(d[0])