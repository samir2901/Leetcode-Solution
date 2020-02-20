def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        value = nums[i+1]
        result += [value]*freq        
    return result
      

print(decompressRLElist([1,2,3,4]))




