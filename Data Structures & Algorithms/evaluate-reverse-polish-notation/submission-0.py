class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack 
        # maybe use hashmap to store the operands?

        # [* 3 + 1 2] -> 2 + 1 = 3 * 3 = 9

        # tokens = ["4","13","5","/","+"]
        # [+  / 5 13 4] -> 4 13 5 / +->
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())

            elif c == '-':  
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)


            elif c == '*': 
                stack.append(stack.pop() * stack.pop())   

            elif c == '/':  
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))    
        return stack[0]        
  