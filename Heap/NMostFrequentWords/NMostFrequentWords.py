# Problem: Find the most n frequent words in a terabytes of strings

# Functions

import heapq

def findMostFrequentWords(words, topIndex):
    if not words:
        raise Exception("Words cannot be empty")

    frequencies = getWordFrequencies(words)
    heap = []

    for word, frequency in frequencies.items():
        if len(heap) < topIndex:
              heapq.heappush(heap, (frequency, word))
        else:
            currentMin = heap[0][0]
            if currentMin < frequency:
                heapq.heappop(heap)
                heapq.heappush(heap, (frequency, word))

    return sorted(heap, reverse = True)

def getWordFrequencies(words):

    frequencies = {}
    for word in words:
        if not word in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    return frequencies

# Main Program
words = ["test", "this", "is", "book", "test", "book", "test", "is", "apple", "android", "windows",
         "apple", "calculator", "facebook", "book", "pc", "phone", "nexus", "android", "apple",
         "ios", "apple", "test", "apple"]

result = findMostFrequentWords(words, 3)
print("Items: %s" %result)
