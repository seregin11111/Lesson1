from Lesson4_Leven import LevenshteinDistance

first_word = 'kitten'
test_words = ["smitten", "mitten", "kitty", "fitting", "written"]


if __name__ == "__main__":
    for word in test_words:
        dist = LevenshteinDistance(first_word, word)
        print("Distance between \(first_word) and \(word): \(dist)")
