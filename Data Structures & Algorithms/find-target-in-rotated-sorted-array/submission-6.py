class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m 
            #Hay que saber si el lado izq está ordenado
            if nums[l] <= nums[m]:
                #Si está ordenado, ahora hay que saber donde buscar el target
                if target < nums[l] or nums[m] < target:
                    #Significa que el target está por el otro lado
                    l = m + 1
                else:
                    r = m - 1
            else:
                #Si está ordenado del lado derecho hay que buscar el target
                if target > nums[r] or target < nums[m]:
                    #Significa que está del lado izq
                    r = m - 1
                else:
                    l = m + 1
        return -1 