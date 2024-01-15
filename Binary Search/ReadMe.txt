# ----------------Edge Cases------------------------
# 1. The number query occurs somewhere in the middle of the list cards.
# 2. query is the first element in cards.
# 3. query is the last element in cards.
# 4. The list cards contains just one element, which is query.
# 5. The list cards does not contain number query.
# 6. The list cards is empty.
# 7. The list cards contains repeating numbers.
# 8. The number query occurs at more than one position in cards.

# ---------------Test Cases------------------------
tests=[]
# 1. The number query occurs somewhere in the middle of the list cards.
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}
tests.append(test)

# 2. query is the first element in cards.
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# 3. query is the last element in cards.
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# 4. The list cards contains just one element, which is query.
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# 5. The list cards does not contain number query.
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# 8. The number query occurs at more than one position in cards.
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# 7. The list cards contains repeating numbers.
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})