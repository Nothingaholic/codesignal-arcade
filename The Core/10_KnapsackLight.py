"""
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, 
and the second item weighs weight2 and is worth value2. 
What is the total maximum value of the items you can take with you, 
assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, 
i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
solution(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
solution(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
solution(value1, weight1, value2, weight2, maxW) = 7.

You can't take both items, but you can take any of them.
"""
def solution(value1, weight1, value2, weight2, maxW):
    total_weight = weight1 + weight2
    max_value = 0
    if total_weight <= maxW:
        max_value = value1 + value2
    else:
        if weight1 <= maxW and weight2 <= maxW:
            max_value = max(value1, value2)
        elif weight1 <= maxW:
            max_value = value1
        elif weight2 <= maxW:
            max_value = value2
    
    return max_value

print(solution(10,5,6,4,9))
print(solution(5,3,7,4,6))
print(solution(10,2,11,3,1))
print(solution(15,2,20,3,2))