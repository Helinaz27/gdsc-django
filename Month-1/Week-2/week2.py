def sum_list(nums):
    return sum(nums)

print("Even numbers between 1 and 20:")
for num in range(2, 21, 2):
    print(num, end=" ")
print("\n")  

def find_largest(nums):
    return max(nums)

nums = [12, 45, 78, 23, 89, 56]
print("Sum of the list:", sum_list(nums))
print("Largest number in the list:", find_largest(nums))
