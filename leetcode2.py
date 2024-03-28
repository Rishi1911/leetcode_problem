'''For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""      '''
class solution(object):
    def gcdOfStrings(self,str1, str2):
        #print(str1,str2)
        len1,len2=len(str1),len(str2)
        for l in range(min(len1,len2),1,-1):
            if len1 % l==0 and len2 % l==0:
                f1,f2 = len1//l,len2//l
                if str1[:l]*f1 == str1 and str1[:l]*f2 == str2:
                    print(str1[:l])
                else:
                    print("rishi")
                break
s = solution()
s.gcdOfStrings("leet",'code')
s.gcdOfStrings("abcabc",'abc')
s.gcdOfStrings("ababab",'abab')
