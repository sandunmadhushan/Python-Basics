# Manipulating Strings

# You are making a text editor and need to implement find/replace functionality.
# The code declares a text string. You need to take two string inputs, which represent the substring to find and what to replace it with in the text.
# Your program needs to output the number of replacements made, along with the new text.

# For example, for the given text "I weigh 80 kilograms. He weighs 65 kilograms.":

# Sample Input
# kilograms
# kg

# Sample Output
# 2
# I weigh 80 kg. He weighs 65 kg.

# The program replaced 2 occurrences of the word kilograms with kg.
# Note, that you need to output the number of replacements, before the replaced text.

text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."
a=input()
b=input()
print(text.count(a))
print(text.replace(a,b))
