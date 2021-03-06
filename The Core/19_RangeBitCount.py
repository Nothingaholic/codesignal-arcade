"""
You are given two numbers a and b where 0 ≤ a ≤ b. 
Imagine you construct an array of all the integers from a to b inclusive. 
You need to count the number of 1s in the binary representations of all the numbers in the array.

Example

For a = 2 and b = 7, the output should be
solution(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. 
Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], 
which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

"""



def solution(a,b):
    ans = 0
    for x in range(a, b+1):
        ans += bin(x).count('1') # convert the number to binary and only count #1
    return ans

# bruce force
# def solution(a,b):
#     arr = []
#     while a <= b:
#         arr.append(a)
#         a += 1
#     binary_arr = ["{0:b}".format(i) for i in arr]
#     ans = 0
#     for numb in binary_arr:
#         for i in numb:
#             ans += int(i)
#     return ans

print(solution(2,7))