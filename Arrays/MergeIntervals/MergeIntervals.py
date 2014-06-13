# Problem: Merge intervals
# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Functions
def merge(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key = lambda tup:tup[0])

    result = []
    previous = sorted_intervals[0]
    for current in sorted_intervals[1:]:
        if previous[1] >= current[0]:
            merged = (previous[0], max(previous[1], current[1]))
            previous = merged
        else:
            result.append(previous)
            previous = current

    result.append(previous)

    return result

# Main program
intervals = [(2,6),(8,10),(15,18),(1,3)]
print(intervals)
print(merge(intervals))
