s = '12abcd405'
no_digits = []
# Iterate through the string, adding non-numbers to the no_digits list
for i in s:
    if i.isdigit():
        no_digits.append(i)

# Now join all elements of the list with '', 
# which puts all of the characters together.
result = ''.join(no_digits)
print result