import re
a = re.sub(r'\W', '', input()).lower()
print(True if a==a[::-1] else False)
