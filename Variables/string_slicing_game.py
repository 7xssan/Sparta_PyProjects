original_word = "flabbergasted"
scrambled_word = "gastaflbered"

hint1_slice = original_word[4:6]
hint2_slice = original_word[-3:]
hint3_slice = original_word[:3]
hint4_slice = original_word[8:10]

print(f"Scrambled word: {scrambled_word}")
print("Now guess the original word from the given scrambled word.")
print("Here are some hints: ")

# hints based on list slicing

print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")

print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")

print("Hint 3: The first 3 letters are '" + hint3_slice + "'.")

print("Hint 4: The 9th and 10th letters are '" + hint4_slice + "'.")

# End of game

print("What's your guess?")