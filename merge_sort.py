#!/usr/bin/env python3


def merge_sort(nums):
    if(len(nums) == 1 or len(nums) == 0):
        return nums

    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


def merge(l, r):
    mergeList = []

    while(len(l) != 0 and len(r) != 0):
        if(l[0] < r[0]):
            mergeList.append(l[0])
            l.remove(l[0])
        else:
            mergeList.append(r[0])
            r.remove(r[0])

    if(len(l) == 0):
        mergeList += r
    else:
        mergeList += l

    print("               ", mergeList)

    return mergeList


def main():
    nums = [1, 10, 8, 1, 12, 9, 31, 2, -1]
    print("Unsorted Array:", nums)
    nums = merge_sort(nums)
    print("Sorted Array:  ", nums)


if __name__ == "__main__":
    main()
