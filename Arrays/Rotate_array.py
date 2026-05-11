class Solution:
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.
        """

        # Length of array
        n = len(nums)

        # If k is greater than array size
        # Example: n = 7, k = 10
        # 10 % 7 = 3
        k = k % n

        # Take last k elements
        # nums[-k:]
        # Example: [1,2,3,4,5,6,7]
        # k = 3
        # Output: [5,6,7]

        last_part = nums[-k:]

        # Take remaining first elements
        # nums[:-k]
        # Output: [1,2,3,4]

        first_part = nums[:-k]

        # Combine both parts
        rotated = last_part + first_part

        # Update original array
        nums[:] = rotated