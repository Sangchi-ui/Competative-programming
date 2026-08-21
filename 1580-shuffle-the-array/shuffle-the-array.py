class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        shuffle_list = []
        list1 = nums[0:n]
        list2 = nums[n:]
        while i < n:
            shuffle_list.append(list1[i])
            shuffle_list.append(list2[i])
            i += 1
        return shuffle_list