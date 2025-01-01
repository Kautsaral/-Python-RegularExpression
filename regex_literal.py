import re

text = "Saya memiliki seekor kucing dan anjing yang lucu"
pattern = r"kucing"

match = re.search(pattern, text)
if match :
    print(match.group())