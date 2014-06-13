# Problem: Insert interval

#Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

#Example 1:
#Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

#Example 2:
#Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

#This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Function

def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]

    result = []
    for current in intervals:
        if current[1] < newInterval[0]:
            result.append(current)
        elif current[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = current
        else:
            newInterval = (min(current[0],newInterval[0]), max(current[1], newInterval[1]))

    result.append(newInterval)

    return result

# Main program
print(insert([(1,3),(6,9)],(2,5)))
print(insert([(1,2),(3,5),(6,7),(8,10),(12,16)],(4,9)))