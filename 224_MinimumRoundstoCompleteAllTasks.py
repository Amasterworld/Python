class Solution:
    def minimumRound(self, tasks : list([int])) ->int:
        
        min_round = 0;
        freq_num = Counter(tasks)
        for num, freq in freq_num.items():
            
            if (freq == 1):
                return -1;
            
            else:
                min_round = freq//3 if freq % 3 == 0 else freq//3 +1;
                # min_round = freq%3 == 0 ? freq/3 : freq/3 +1; C++
        return min_round;