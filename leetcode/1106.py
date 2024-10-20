# 1197 Parsing A Boolean Expression
# https://leetcode.com/problems/parsing-a-boolean-expression/ - Hard


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        operands_stack: list[list[bool]] = [[]]
        operators:list[str] = [] 

        char_index = 0
        while char_index < len(expression):
            char = expression[char_index]

            if char in "!|&":
                operators.append(char)
                operands_stack.append([])
                # skip opening bracket so extra char
                char_index += 2
                continue

            if char == ")":
                operator = operators.pop()
                booleans = operands_stack.pop()

                match operator:
                    case "!":
                        # add one level lower
                        operands_stack[-1].append((not booleans[0])) # should only be 1 elem here

                    case "|":
                        res = booleans[0]
                        for boolean in booleans:
                            res = res or boolean
                        operands_stack[-1].append(res)

                    case "&":
                        res = booleans[0]
                        for boolean in booleans:
                            res = res and boolean
                        operands_stack[-1].append(res)


            if char == "f":
                operands_stack[-1].append(False)
            elif char == "t":
                operands_stack[-1].append(True)
            else:
                # comma or space in between booleans
                pass
            
            char_index += 1
    
        return operands_stack[0][0]
