from typing import List

# 12/31/2021
class Solution1:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		pair_indices = {}
		for i, num in enumerate(nums):
			if num in pair_indices:
				return [pair_indices[num], i]
			pair_indices[target - num] = i

i# 12/31/2021
class Solution2:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		pair_indices = {}
		for i, num in enumerate(nums):
			if num in pair_indices:
				return [pair_indices[num], i]
			elif target - num in nums:
				pair_indices[target - num] = i

#print(Solution1().twoSum([1, 2, 4 , 5, 2, 4], 6))
print(Solution2().twoSum([1, 2, 4 , 5, 2, 4], 6))
