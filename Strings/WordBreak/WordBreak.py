# Problem: Word Break string
# e.g. "Thisisatest" = > "This is a test"

# Utility class
class WordBreaker:
    def __init__(self):
        self.words = {"this", "is", "a", "test"}

    def wordBreak_dp(self, sentence):
        if not sentence:
            return False

        dp =[False] * (len(sentence) + 1)
        dp[len(sentence)] = True

        for index in range(len(sentence), -1, -1):
            suffix_index = index
            while suffix_index < len(sentence):
                suffix = sentence[index:suffix_index + 1]
                if suffix in self.words and dp[suffix_index + 1]:
                    dp[index] = True
                    break
                suffix_index += 1

        return dp[0]

    def wordBreak_recursive(self, word):
        if word in self.words:
            return True

        for index in range(1, len(word)):
            prefix = word[:index]
            if prefix in self.words:
                suffix = word[index:]
                can_wordbreak = self.wordBreak_recursive(suffix)
                if can_wordbreak:
                    return True

        return False

# Main program
wb = WordBreaker()
print(wb.wordBreak_recursive("thisisatest"))
print(wb.wordBreak_dp("thisisatest"))



