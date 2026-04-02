class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                sumAcc = numbers[mid] + numbers[i]

                if sumAcc < target:
                    l = mid + 1
                elif sumAcc > target:
                    r = mid - 1
                else:
                    return [i+1,mid+1]
        return []