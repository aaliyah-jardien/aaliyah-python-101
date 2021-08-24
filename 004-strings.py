# strings are plain texts
print("Life\nChoices")
print("Coding\"Academy")
print("Life\Is\Beautiful")

# creating a string variable
phrase = "The Butterfly Effect"
print(phrase)

# concatenation
# appending a string and
# adding another string on it
print(phrase + " is the phenomenon whereby a minute localized change in a complex system can have large effects elsewhere.")

# running functions to modify strings
# also using functions to get info from strings
print(phrase.lower())
print(phrase.upper())
# checking whether the phrase is in lower or upper case
print(phrase.islower())
print(phrase.upper().isupper())

# checking the length of a string
print(len(phrase))

# specifying the index of the character i want
print(phrase[11])
# index starts with zero

# index function
# tells me where a specific character is found in a string
# passing a parameter
# a value given to a function
print(phrase.index("fly"))

# replace process
print(phrase.replace("Effect", "Process"))
