#TC is O(n)
#SC also is O(n);
from collections import Counter
class Solution:
    def minimumRounds(self, tasks : list([int])) ->int:
        
        min_round = 0;
        freq_num = Counter(tasks)
        for num, freq in freq_num.items():
            
            if (freq == 1):
                return -1;
            
            else:
                min_round += freq//3 if freq % 3 == 0 else freq//3 +1;
                # min_round += freq%3 == 0 ? freq/3 : freq/3 +1; C++
        return min_round;

if __name__ == '__main__':
    
    myObj = Solution();
    tasks_1 = [2,2,3,3,2,4,4,4,4,4]
    tasks_2 = [2,3,3]
    print(myObj.minimumRounds(tasks_1));
    print(myObj.minimumRounds(tasks_2));