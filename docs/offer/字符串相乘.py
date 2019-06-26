class Solution:
    # 此题不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
    # 所以我用的方法是把字符转ASCII码方法运算，比如："1"的ASCII码是49  ASCII码转换为int：ord('A')
    # int转为ASCII码：chr(65)
    # TypeError: 'int' object is not iterable
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :return: str
        """
        # 首先分别得到两个字符串的每个字符，并用列表保存
        num1_str_list = list(num1)
        num2_str_list = list(num2)
        # 这一步是本题的考点了，将每个字符转化成相应的ASCII码，ASCII码是整数类型
        num1_int_list = [ord(index)-48 for index in num1_str_list]
        num2_int_list = [ord(index)-48 for index in num2_str_list]
        # 得到了这两个字符串对应每个位置上字符的ASCII码后，现在就可以将每个字符串所对应的整数表示出来了
        num1_sum = 0
        num2_sum = 0
        for num1_index in range(len(num1_int_list)):
            num1_sum += num1_int_list[num1_index] * 10**(len(num1_int_list) - num1_index - 1)
        for num2_index in range(len(num2_int_list)):
            num2_sum += num2_int_list[num2_index] * 10**(len(num2_int_list) - num2_index - 1)
        # 接下来直接将两个字符串对应的整数相乘得到结果
        final_result = num1_sum * num2_sum

        # 接下来就是要把得到的整数类型的结果转化为str字符串类型了
        # 第一步是要得到final_result每一位的数，并保存起来
        answer_int_list = []
        if final_result > 0:
            while final_result > 0:
                indice = final_result % 10
                answer_int_list.append(indice)
                final_result = final_result // 10
            # 因为我们是从个位数开始存放数组的，所以得将这个answer_int_list逆序排列得到原始数据的正常排列
            answer_int_list.reverse()
        else:
            answer_int_list.append(final_result)
        # 第二步就是要将每一个整数转化成相应的ASCII码
        answer_str_list = [chr(index+48) for index in answer_int_list]
        return ''.join(answer_str_list)


if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    result = Solution().multiply(num1, num2)
    print(result)