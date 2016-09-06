#Nestor Alvarez

import string # for special string data
letters = list(string.ascii_letters)

# nums is a range object
nums = range(1, 101)

# We can create a nums is a list as follows
# nums = list(range(1, 101))

complex = [(i * 3j) for i in range(1,11)]

#Ex 1
print(list(complex[i] * complex[i] for i in range(0,10)))

#Ex 2
print(list(letters[i] * 5 for i in range(0, 52)))

nums_list = list(nums[i] * 0 for i in range(0, 1))
nums_list.extend(list(nums[i] * nums[i-1] for i in range(1, 100)))

#Ex 3
print(nums_list) 

nums = list(nums)
nums.insert(0,0)

#Ex 4
print(nums)

#Ex 5
print(list(nums[i] for i in range(0,102, 3)))
