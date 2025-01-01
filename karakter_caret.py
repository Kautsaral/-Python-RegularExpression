import re

text = "kucing yang lucu"
pattern = r"^kucing"

match = re.search(pattern, text)

if match:
    print(match.group())