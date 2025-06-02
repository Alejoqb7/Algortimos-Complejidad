#Profe para este la verdad me apoyé de este repo https://github.com/Jeffma0103/Letter-Combinations-of-a-Phone-Number/blob/main/Letter_Combinations_of_a_Phone_Number.py

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        phone = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def run(s ,ans):
            tmp = []
            if ans == []:
                for i in phone[s]:
                    tmp.append(i)
            else:
                for i in range(len(ans)):
                    for j in phone[s]:
                        tmp.append(ans[i]+j)
            return tmp
        
        for i in digits:
            ans = run(i,ans)
            
        return ans