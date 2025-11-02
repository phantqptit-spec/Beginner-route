S = 'I have 8 friends inside my heart. I have 0 friend in life. '
S1 = S.split()  # split into words
punctuation = ",./<>?;:|~!@$%^&*()_+-="

# Create a string to hold the cleaned sentence
S_clean = ""

for word in S1:
    clean_word = word
    for p in punctuation:
        clean_word = clean_word.replace(p, "")  # remove punctuation
    # Add the cleaned word to the result string with a space
    S_clean += clean_word + " "

# Remove the extra space at the end
S_clean = S_clean.strip()

print(S_clean)
