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


"""
12 contains 2 digits (even number of digits)
345 contains 3 digits (odd number of digits)
2 contains 1 digits (odd number of digits)
6 contains 1 digits (odd number of digits)
7896 contains 4 digits (even number of digits)
555 contains 3 digits (odd number of digits)
901 contains 3 digits (odd number of digits)
482 contains 3 digits (odd number of digits)
1771 contains 4 digits (even number of digits)
There are 3 numbers(s) from the list contain an even number of digits
"""
