import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    count = 0
    for i in range(n):
        # 读取每一行
        word = str(sys.stdin.readline().strip())
        if word == word[::-1]:
            count += 1
