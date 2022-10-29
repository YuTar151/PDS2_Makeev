

string = 'fgfhsadsssssllfd'
counted_chars = {}

for char in string:
    if char in counted_chars:
        counted_chars[char] += 1
    else:
        counted_chars[char] = 1

print(max(counted_chars))