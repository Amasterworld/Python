#The algorithm to solve this problem is the same version used for C++, note that ";" are not necessary in Python
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        l  = 0;
        r = len(s) - 1;
        vowels = set(list("ueoaiUEOAI"));
        while l < r:
            while l < r  and s[r] not in vowels:
                r -= 1;
            while l < r  and s[l] not in vowels:
                l += 1;

            # we cannot s[r], s[l] = s[l], s[r] because s is a string that is immutable -> but we can convert s to list and swap
            #another solution is: concatenate the string
            if (s[l] != s[r]):
                s = s[:l] + s[r] + s[l+1: r] + s[l] + s[r+1:];
            l += 1;
            r -= 1;
        
        return s;

if __name__ ==  "__main__":
    myObj = Solution();
    str_1 = "leetcode";
    str_2 = "Aa";
    print(myObj.reverseVowels(str_1)) # leotcede
    print(myObj.reverseVowels(str_2)) # aA
