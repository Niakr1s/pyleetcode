class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            match (ch):
                case "(":
                    stack.append(")")
                case "[":
                    stack.append("]")
                case "{":
                    stack.append("}")
                case ")" | "]" | "}":
                    if len(stack) == 0 or ch != stack.pop():
                        return False
        return len(stack) == 0
