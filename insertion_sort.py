#!/usr/bin/env python3

def insertion_sort(nums):
    for i in range(1, len(nums)):
        value_to_insert = nums[i]
        insert_position = i

        while insert_position > 0 and nums[insert_position - 1] > value_to_insert:
            nums[insert_position] = nums[insert_position - 1]
            insert_position = insert_position -1

        nums[insert_position] = value_to_insert
        print("               ", nums)  # prints each iteration

def main():
    nums = [1, 10, 8, 1, 12, 9, 31, 2]
    print("Unsorted Array:", nums)
    insertion_sort(nums)
    print("Sorted Array:  ", nums)

if __name__ == "__main__":
    main()
