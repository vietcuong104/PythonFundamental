from difflib import SequenceMatcher

text1 = "This is BingBoong, she is my first girlfriend"
text2 = "BingBoong is also my wife now"

sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")