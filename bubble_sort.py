#!/usr/bin/env python3


def swap(li, x, y):
    li[x], li[y] = li[y], li[x]


def bubble_sort(nums):
    for i in range(0, len(nums)-1):
        swapped = False
        for j in range(0, len(nums)-1):
            if(nums[j] > nums[j+1]):
                swap(nums, j, j+1)
                swapped = True
                print("               ", nums)

        if(not swapped):
            break


def main():
    nums = [1, 10, 8, 1, 12, 9, 31, 2]
    print("Unsorted Array:", nums)
    bubble_sort(nums)
    print("Sorted Array:  ", nums)


if __name__ == '__main__':
    main()
