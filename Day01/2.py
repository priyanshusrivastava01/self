# VowelorConsonant–Checkwhetheragivenalphabetisvowelorconsonant.

ch = input("Enter the Character: ")

# asv = ord(ch)

# if (asv == 65 or 69 or 73 or 79 or 85 or 97 or 101 or 105 or 111 or 117):
#     print("Vowel")
# else:
#     print("Consonant")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")