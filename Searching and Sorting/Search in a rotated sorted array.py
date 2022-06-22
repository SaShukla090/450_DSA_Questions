class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        pivot = self.searchPivot(nums)

        real_index = self.binarySearch(nums,pivot,target)

        return real_index



        # if real_index >= pivot:
        #     index = real_index - pivot
        # elif real_index < pivot:
        #     index = len(num) - real_index - pivot
        # return index

    def searchPivot(self, num):
        n = len(num)
        start = 0
        end = len(num) - 1


        while True:

            mid = (end - start)//2 + start
            if n == 2:
                if num[0]<num[1]:
                    return 0
                else:
                    return 1

            if mid == 0:
                if num[mid] < num[mid + 1]:
                    pivot = mid
                    break
            if mid == n-1:
                if num[mid -1] > num[mid]:
                    pivot = mid
                    break
                # pivot = mid
                # break
            if num[mid-1]>num[mid]<num[mid+1]:
                pivot = mid
                break
            elif num[mid] > num[n-1]:
                start = mid + 1
            elif num[mid] < num[n-1]:
                end = mid - 1

            if end < start:
                break

        return pivot

    def binarySearch(self, num, pivot, target):
        n = len(num)
        start = 0
        end = pivot
        while True:
            mid = (end - start)//2 + start
            if num[mid] == target:
                r_index = mid
                return r_index
                break
            elif num[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

            if end<start:
                break

        start = pivot
        end = n-1
        while True:
            mid = (end - start)//2 + start
            if num[mid] == target:
                r_index = mid
                break
            elif num[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

            if end<start:
                r_index = -1
                break

        return r_index












list = [5,1,2,3,4]
target = 1
s = Solution()
x = s.search(list, target)
print("The answer = ", x)