def leapYear():
    year = int(input("Enter a year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Year", year, "is a leap year")
    else:
        print("Year", year, "is not a leap year")

leapYear()

def checkVowelOrConsonant(char):
    # Convert the character to lowercase for case insensitivity
    char = char.lower()

    if char in "aeiou":
        print(char, "is a vowel.")
    elif char.isalpha():
        print(char, "is a consonant.")
    else:
        print(char, "is neither a vowel nor a consonant.")

# Get a character from the user
character = input("Enter a character: ")

# Check if it's a vowel or consonant
checkVowelOrConsonant(character)