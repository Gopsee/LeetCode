class Solution
    def singleNumber(self, nums List[int]) - int
        Table = list()
        for i in range(len(nums))
            if (nums[i] in Table)
                Table.remove(nums[i])
            elif (nums[i] not in Table)
                Table.append(nums[i])
        return Table[0]