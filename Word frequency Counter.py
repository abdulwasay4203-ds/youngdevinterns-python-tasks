# Count the frequency of each word in a text

text = input("Enter text: ").lower()

words = text.split()
frequency = {}      # dictionary to store word counts

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
