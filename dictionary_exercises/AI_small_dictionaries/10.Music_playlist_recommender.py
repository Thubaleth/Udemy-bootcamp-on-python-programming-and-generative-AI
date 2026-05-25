
"""
Recommend songs by mood.

songs = {
    "Happy": ["Happy Song", "Good Vibes"],
    "Sad": ["Blue Sky", "Lonely Night"],
    "Workout": ["Power Up", "Run Fast"]
}

Requirements:
- Ask user for mood
- Recommend matching songs
- Display playlist
"""
songs = {
    "Happy": ["Happy Song", "Good Vibes"],
    "Sad": ["Blue Sky", "Lonely Night"],
    "Workout": ["Power Up", "Run Fast"]
}
def Recommend_songs():
    
    mood = input("Enter the mood: ")

    for key,lst in songs.items():

        if key == mood:
            print(f"recommended songs is {[lst]}")

Recommend_songs()

