class Solution():
    def __init__(self):
        self.address = []
    def restoredip(self, s):
        if len(s)<4 or len(s)>12:
            return self.address
        self.corerestore([], s)
        return self.address
    def corerestore(self, address, s):
        if len(address)==4 and len(s)==0:
            address_str = '.'.join(address)
            if address_str not in self.address:
                self.address.append(address_str)
            return
        for index in range(3):
            if len(s)>=index+1:
                one_str = s[:index+1]
                if int(one_str)<256 and str(int(one_str))==one_str:
                    self.corerestore(address+[one_str], s[index+1:])
if __name__ == "__main__":
    S = Solution()
    s = input()
    res = S.restoredip(s)
    print(','.join(res))