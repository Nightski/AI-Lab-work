sentence = "Sort the sentence in alphabetical order python"

words = sentence.split()

sorted_words = sorted(words, key=str.lower)

sorted_sentence = ' '.join(sorted_words)

print("Original sentence:", sentence)
print("Alphabetically sorted sentence:", sorted_sentence)