#!/usr/bin/env python3


def swap(li, x, y):
    li[x], li[y] = li[y], li[x]


def selection_sort(nums):
    for i in range(0, len(nums)-1):
        min_index = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        swap(nums, i, min_index)
        print(nums)


def main():
    nums = [1, 10, 8, 1, 12, 9, 31, 2]
    print("Unsorted Array:", nums)
    selection_sort(nums)
    print("Sorted Array:  ", nums)


if __name__ == "__main__":
    main()
