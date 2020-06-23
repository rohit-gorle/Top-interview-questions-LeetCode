class Solution:
    def reverse(self, x):
        m = 1
        if x < 0:
            m = -1
            yx = str(x)[1:]
        else:
            yx = str(x)

        x = int(yx[::-1])
        
        return 0 if x > pow(2, 31) else x * m
