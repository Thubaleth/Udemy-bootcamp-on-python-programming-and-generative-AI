"""
Count word frequencies from a text file.

Example file:
story.txt

Requirements:
- Open and read file
- Split text into words
- Count word frequencies
- Display top 5 most common words
- Save results to output.txt
"""
count_word = {}

with open("story.txt") as f:
    words = f.read().split()
    for word in words:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
        
    
# Sort words by frequency (highest first)
top_words = sorted(count_word.items(),
                   key=lambda x: x[1],
                   reverse=True)

# Get top 5 words
top_5 = top_words[:5]

# Display results
print("Top 5 Most Common Words:\n")

for word, count in top_5:
    print(f"{word}: {count}")

# Save results to output.txt
with open("output.txt", "w") as out:
    out.write("Top 5 Most Common Words:\n\n")

    for word, count in top_5:
        out.write(f"{word}: {count}\n")

print("\nResults saved to output.txt")
    


        

    


