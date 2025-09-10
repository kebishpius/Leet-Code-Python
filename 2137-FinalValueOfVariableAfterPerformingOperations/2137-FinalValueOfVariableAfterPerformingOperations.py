# Last updated: 9/10/2025, 12:55:50 AM
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in range(len(operations)):
            if operations[i] == "--X":
                x=x-1
            elif operations[i] == "X--":
                x=x-1
            elif operations[i] == "X++":
                x=x+1
            elif operations[i] == "++X":
                x=x+1
            else:
                pass
        return x
        