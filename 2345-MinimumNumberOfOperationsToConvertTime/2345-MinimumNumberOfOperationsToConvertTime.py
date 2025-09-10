# Last updated: 9/10/2025, 12:55:32 AM
class Solution(object):
    def convertTime(self, current, correct):
        current = (60 * int(current[0:2])) + int(current[3:])
        correct = (60 * int(correct[0:2])) + int(correct[3:])
        print(correct)
        ops = 0
        while current < correct:
            if current + 60 <= correct:
                current += 60
                ops += 1
            elif current + 15 <= correct:
                current += 15
                ops += 1
            elif current + 5 <= correct:
                current += 5
                ops += 1
            else: 
                current += 1
                ops += 1
            if current == correct:
                return ops
        return ops

        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        