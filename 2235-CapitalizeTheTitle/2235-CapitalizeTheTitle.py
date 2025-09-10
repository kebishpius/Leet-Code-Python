# Last updated: 9/10/2025, 12:55:43 AM
class Solution(object):
    def capitalizeTitle(self, title):
        x = title.split(" ")
        for i in range(len(x)):
            if len(x[i]) == 1 or len(x[i]) == 2:
                x[i] = x[i].lower()
            else:
                x[i] = x[i].lower()
                x[i] = x[i].title()
        ans = ""
        for j in x:
            ans += j + " "
        return ans[0:len(ans)-1]
        

        """
        :type title: str
        :rtype: str
        """
        