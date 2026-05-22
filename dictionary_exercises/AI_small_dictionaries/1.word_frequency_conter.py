"""Count how many times words appear in text.

Example:
Input:
"AI is fun and AI is powerful"

Output:
{
    "AI": 2,
    "is": 2,
    "fun": 1,
    "and": 1,
    "powerful": 1
}

Requirements:
- Split sentence into words
- Use dictionary to count frequencies
- Display most common word
"""

def word_counter():
    sentence = "AI is fun and AI is powerful"
    new_sentence = sentence.split()
    
    counts = {}
    for word in new_sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts
      
    
print(word_counter())