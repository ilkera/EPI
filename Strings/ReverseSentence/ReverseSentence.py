# Problem: Reverse a sentenec
# e.g. "This is a test" => "test a is This"

# Functions
def reverseSentence(sentence):
    if not sentence:
        return

    sentenceList = list(sentence)

    # Reverse all sentence
    reverse(sentenceList, 0, len(sentence) - 1)

    index = 0
    start = 0
    end = 0
    while index < len(sentenceList):
        if sentenceList[index] == " ":
            end = index - 1
            reverse(sentenceList, start, end)
            start = index + 1
        index += 1

    end = index - 1
    reverse(sentenceList, start, end)

    return "".join(sentenceList)

def reverse(word, startIndex, endIndex):
    while startIndex < endIndex:
        temp = word[startIndex]
        word[startIndex] = word[endIndex]
        word[endIndex] = temp
        startIndex += 1
        endIndex -= 1

# Main program
sentence = "This is a test"
print("Sentence: %s => Reversed: %s" %(sentence, reverseSentence(sentence)))