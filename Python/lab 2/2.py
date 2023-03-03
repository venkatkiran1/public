class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        diff=skill[len(skill)-1]+skill[0]
        result=0
        while i<j:
            if skill[j]+skill[i]==diff:
                result=result+skill[j]*skill[i]
            else:
                return -1
            i+=1
            j-=1
        return result