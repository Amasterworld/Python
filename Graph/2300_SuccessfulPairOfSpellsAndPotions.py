"""
2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
"""

"""
SOLUTION: this problem can easily be solved if we use two for loop nested 
like this : for spell in spells:
                for potion in potions:
                    if spell * potion >= success:
                        cnt += 1
                ans.append(cnt)
            return ans;
O(n*m) where n and m are length of spell in potions, repectively.

->optimize the solution: sort the potions . potions.sort(reverse = True) from highest value to smallest value

for i in range(n)
    j = 0
    while j < m and spell[i] * potions[j] >= success:
        j += 1
    ans.append(j)
this approach is little better, because potions vector/list is sorted when whenevr spell[i] * postion[j] < success
->Stop and appendto ans
but  is  TLE (Time limited Exceed )

So, need to optinmize more, now we see:
after sorting the potions array, sorted_postions = [5,4,3,2,1] ,spell = [5,1,3], success = 7
spell[0] = 5, success/spell[0] = 7/5 = 1.4, that mean sorted_postions[j] >= 2 (because they are interger numbers, hecen 1.4->2)
is what we must count or know how many sorted_postions[j] >= 2. now the problem will be binary search:
given an number and return the most left idx that satisfies the given condtion.
in the above example, if we know the the most left idx that position[idx] >=2 is 1 hence we only need to calculate
len(positions) - idx = 5-1 = 4. 4 number in positions can be >= success.
now how to determine index of the valid_num, valid_num =  success/spell[i]? unfortunately, it is not correct answer, 
as we see, valid_num is an interger number, so we need to round up it to the closest interger. so we need to adding
spell[i] - 1, then valid_num = (success + spell[i] - 1)/spell[i] to ensure that the index is always rounded up to the nearest integer. 

when we get the valid_num only need to put it in the binary search function for positions to get its index


"""

class Solution:
    
          
    class Solution:
    
          
        def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

            n = len(spells)
            m = len(potions)
            #sort the postion from hightest to the smallest value
            potions.sort(reverse = False)
            

            ans = []
            #b_s is an abreviation of binary search
            #note that if you want, you can use the build in function binary search: see below
            def b_s(idx):
                l = 0
                r = m
                print("idx ", idx)
                while l < r:
                    mid = l + (r-l)//2
                    
                    if potions[mid] >= idx:
                        print("mid ", mid, "at mid", potions[mid])
                        r = mid
                    else:
                        l = mid + 1
                print("l ", l)
                return l

            for i in range(n):
                
                valid_num = (success + spells[i] - 1) // spells[i]
                
                idx_valid_num = b_s(valid_num)
                print(idx_valid_num)
                ans.append(m - idx_valid_num)
            return ans

#using build in binary search 
import bisect as b_s
class Solution:
    
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        n = len(spells)
        m = len(potions)
        ans =[]
        potions.sort() # if you want to sort in reverse hecne potions.sort(reverse = True)

        for i in range(n):
            
            valid_pos = (success + spells[i] - 1)// spells[i]
            #using binary search to find the idx in potions where potions[idx] >= valid_pos
            idx_valid_pos = b_s.bisect_left(potions, valid_pos)
            ans.append(m - idx_valid_pos)
        
        #idx_valid_pos = b_s.bisect_left(potions, (success + spells[i] - 1)// spells[i])
        #shorter code can be ans.append(m - idx_valid_pos if idx_valid_pos <= m - 1 else 0)
        return ans;
                       
 # the solution is tested in Leetcode engine       






