# Sample input
nums = [12,345,2,6,7896,555,901,482,1771]

# Use sum to count the total numbers of which contain an even number of digits
def findNumbers(nums):
  return sum((len(str(i))) % 2 == 0 for i in nums)

# Text Summary
for num in nums:
  test = len(str(num))
  even_or_odd = lambda x : 'even' if x % 2 == 0 else 'odd'
  print(f'{num} contains {test} digits ({even_or_odd(test)} number of digits)')

print(f'There are {findNumbers(nums)} numbers(s) from the list contain an even number of digits')
  
# if test % 2 == 0:
#   print('(even number of digits)')
# else:
#   print('(odd number of digits)')
