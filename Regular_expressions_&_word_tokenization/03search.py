import re

scene_one = 'the quick brown coconuts is here!'

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\:"

dumytext = 'the quick.. brown: [coconuts] is here!....'
print(re.search(pattern1, dumytext))

# Use re.search to find the first text in square brackets
print(re.search(r"\[.*\]", dumytext))

# Find the script notation at the beginning of the sentence
scene_one = [
    "This is the first sentence.",
    "Here is the second sentence.",
    "This is the third sentence.",
    "Narrator: This is the fourth sentence with a script notation.",
    "This is the fifth sentence."
]

pattern2 = r"\w+:"
print(re.match(pattern2, scene_one[3]))





