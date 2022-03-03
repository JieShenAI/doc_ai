# Created by JieShen at 2022/3/3 14:49

class Solution:
    def addDigits(self, num: int) -> int:
        def add(n: int):
            cnt = 0
            while n:
                cnt += n % 10
                n //= 10
            # print(n, cnt)
            return cnt

        while num >= 10:
            num = add(num)
        return num


if __name__ == '__main__':
    num = 7894518  # 6
    digits = Solution().addDigits(num)
    print(digits)
