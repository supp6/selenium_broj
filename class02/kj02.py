nums=[3,11,6,9,12,26,5]
L=len(nums)
for i in range (L-1):
    for j in range (L-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            print('排序后：%s'% nums)
