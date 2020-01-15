class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            potential_target = numbers[left] + numbers[right]
            if potential_target == target:
                return [left + 1, right + 1]
            elif potential_target < target:
                left += 1
            else:
                right -= 1

                
                