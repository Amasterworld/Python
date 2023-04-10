
"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""
import unittest
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        len_str = len(s)
        if len_str == 1: 
            return False
        stack = deque()

        for i in range(0, len_str):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                #print(stack)
                continue;
            if len(stack) == 0:
                return False

            if s[i] == ')' :
                prev_sysm = stack.pop()
                if prev_sysm != '(':
                    return False
            elif s[i] == ']' :
                prev_sysm = stack.pop()
                if prev_sysm != '[':
                    return False
            elif s[i] == '}':
                prev_sysm = stack.pop()
                if prev_sysm != '{':
                    return False
        
        return len(stack) == 0
        return len(stack) == 0 # True if stack is empty, stack.empty() in C++

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.valid_parenthesis = Solution()
    #intended not write: tearDown(self)
    #test some simple  scenarios
    def testEx1_2_3(self):

        s = "()"
        self.assertEqual(self.valid_parenthesis.isValid(s), True)
        s = "()[]{}"
        self.assertEqual(self.valid_parenthesis.isValid(s), True)
        s = "(]"
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
    #test  corner condition when len(s) == 1
    def testCorner(self):

        s = "("
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
        s = "]"
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
        s = "{"
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
    
    def testComplexSce(self):

        s = ")()[]"
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
        #s does not contain any  open symbols
        s = ")]"
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
        #s contain only open symbols 
        s = "[["
        self.assertEqual(self.valid_parenthesis.isValid(s), False)
        s = "([{}])"
        self.assertEqual(self.valid_parenthesis.isValid(s), True)
        
if __name__ == '__main__':

    unittest.main()