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
# tests=[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
#  {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
#  {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
#  {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
#  {'input': {'cards': [6], 'query': 6}, 'output': 0},
#  {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
#  {'input': {'cards': [], 'query': 7}, 'output': -1},
#  {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
#   'output': 7},
#  {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#    'query': 6},
#   'output': 2}]

# ---------------------------CODE-------------------------------
locate_cards(card, query)

def binary_search(low, high, condition):
    while low<=high:
        mid=(low+high)//2
        result = condition(mid)
        if result=="found":
            return mid
        elif result=="left":
            high=mid-1
        else:
            low=mid+1
    return -1

def locate_cards(card, query):
    def condition(mid):
        if card[mid]==query:
            if card[mid-1]==query and mid-1>0:
                return "left"
            else:
                return "found"
        elif card[mid]<query:
            return "left"
        else:
            return "right"
    return binary_search(0, len(card)-1, condition)











