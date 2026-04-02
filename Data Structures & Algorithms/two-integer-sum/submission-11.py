class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            diff = 7 - 3
            diff = 4
            if diff no está en el hash
                hashMap[diff] = index
            else:
                return index, hashMap[diff]
        '''
        hashMap = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff  in hashMap:
                return [hashMap[diff], i]
            hashMap[x] = i
        return