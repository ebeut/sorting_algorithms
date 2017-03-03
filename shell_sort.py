#!/usr/bin/env python3

def shell_sort(nums):
    gap = len(nums) // 2

    while gap > 0:
        for i in range(gap, len(nums)):
            value_to_insert = nums[i]
            insert_position = i

            while insert_position >= gap and nums[insert_position - gap] > value_to_insert:
                nums[insert_position] = nums[insert_position - gap]
                insert_position -= gap

            nums[insert_position] = value_to_insert
            print("               ", nums)  # prints each iteration

        gap //= 2

def main():
    nums = [1, 10, 8, 1, 12, 9, 31, 2]
    print("Unsorted Array:", nums)
    shell_sort(nums)
    print("Sorted Array:  ", nums)

if __name__ == "__main__":
    main()
