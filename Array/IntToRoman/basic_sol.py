class Solution():
    def intToRomam(self, number:int)-> str:
        cache = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 
                90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 
                5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for num in cache:
            res += (number // num) * cache[num]
            number = number%num
        return res

if __name__ =="__main__":
    sol = Solution()
    print(sol.intToRomam(53))
    print(sol.intToRomam(6006))
    print(sol.intToRomam(59))
    print(sol.intToRomam(75))
    print(sol.intToRomam(6000))
    print(sol.intToRomam(603))
    print(sol.intToRomam(607))
