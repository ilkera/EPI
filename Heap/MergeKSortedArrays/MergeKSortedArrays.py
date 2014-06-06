# Problem: Merge k sorted arrays (Arrays have the same length of N)
# e.g. k = 3
# L1 = [1, 4, 7, 12]
# L2 = [2, 6, 10, 15]
# L3 = [3, 5, 8, 11]

# Functions

import heapq

def merge(collectionOfArrays, array_size):
    if not collectionOfArrays:
        return []

    index_list = [0] * array_size
    min_heap, result = [], []

    # Add first items from each collection
    for list_index, current_list in enumerate(collectionOfArrays):
        heapq.heappush(min_heap, (current_list[0], list_index, 0))

    while min_heap:
        min_item = heapq.heappop(min_heap)
        current_value, current_list_index, item_index_in_list = min_item[0], min_item[1], min_item[2]
        result.append(current_value)

        if item_index_in_list + 1 != array_size:
            item_index_in_list += 1
            heapq.heappush(
                min_heap,
                (
                    collectionOfArrays[current_list_index][item_index_in_list],
                    current_list_index,
                    item_index_in_list)
                )

    return result

# Main program
L1 = [1, 4, 7, 12]
L2 = [2, 6, 10, 15]
L3 = [3, 5, 8, 11]

collection = [L1, L2, L3]
result = merge(collection, 4)
print(result)