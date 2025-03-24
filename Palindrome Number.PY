class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=str(x)
        rt,lt=len(st)-1,0
        while rt>=lt:
            if st[rt]==st[lt]:
                rt-=1
                lt+=1
            else:
                return False
        return True