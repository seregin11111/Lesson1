class LevenshteinDistance:
    def levenshtein_distance(first_word: str, second_word: str) -> int:

        if len(first_word) < len(second_word):
            return levenshtein_distance(second_word, first_word)

        if len(second_word) == 0:
            return len(first_word)

        previous_row = list(range(len(second_word) + 1))

        for i, c1 in enumerate(first_word):

            current_row = [i + 1]

            for j, c2 in enumerate(second_word):
                # Считаем
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)

                # Минимальное значение
                current_row.append(min(insertions, deletions, substitutions))

            # сохраняем previous row
            previous_row = current_row

        # Возврат последнего
        return previous_row[-1]

dist = LevenshteinDistance()

if __name__ == "__main__":
    result = LevenshteinDistance(first_word, second_word)
    print(f"Levenshtein distance between {first_word} and {second_word} is {result}")

