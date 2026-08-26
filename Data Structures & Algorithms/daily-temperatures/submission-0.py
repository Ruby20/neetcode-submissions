class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # temp, idx
        output =[0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, stackindx = stack.pop()
                output[stackindx] = i - stackindx

            stack.append([t, i])
        return output    

        