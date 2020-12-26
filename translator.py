
# This small piece of code translates a phrase which contains vowels into a letter "k" .
# For example, the word "Hello" contains 2 vowels, "e" and "o".
# It translates the vowels into "k". So, it's gonna print out "Hkllk".

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
              translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

