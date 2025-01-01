import re

text = "Aku memiliki seekor anjing dan kicing yang lucu"
pattern = r"k.cing"

match = re.search(pattern, text)

if match:
    print(match.group())